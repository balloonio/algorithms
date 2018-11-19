"""

这里主要想分享ATM这道题, 其余和面经都一样

题目是: 给定五个interface(除了display以外, 其余皆为***空的***)

- Display
    - string readInput(string displayText)
    - void showError(string errMsg)
    - void showMessage(string msg)
- AccountStore
- CardHandler
- CashDispenser
- CashInTake

请设计每个interface需要的methods来implement一个ATM以下的功能:
1. createAccount
2. login
3. withdraw
4. deposit. 1point3acres
5. checkBalance
6. logout
...etc

Example
1. createAccount
void createAccount() {. 1point3acres
    string name = _display.readInput("Enter your name");
    string address = _display.readInput("Enter your address");

    // 除了display以外的interface皆为空的, 所以这里containsUser就是你要设计的
    if (_accountStore.containsUser(name, address)) {
        _display.showError("User already exists");
        return;
    }

    string pincode = _display.readInput("Enter pincode");

    // 这里, 我们设计卡片都带有userId, 之后只需要read卡片的userId再让user输入pincode, 即可login
    string userId = _accountStore.createUser(name, address, pincode);

    // ATM会做出一张实体的卡片并带有userId发给user
    _cardHandler.createCard(userId);
}

2. withdraw
void withdraw() {
    // 从卡片中读取userId
    string userId = _cardHandler.readCard();
    string pincode = _display.readInput("Enter pincode");
    if (!_accountStore.verify(userId, pincode)) {
        _display.showError("Invalid card or pincode");
        return;
    }
. 1point3acres
    string amountStr = _display.readInput("Enter withdraw amount");
    int amount = int.parse(amountStr);

    // 扣除这个user的balance, 如果余额不足, 则不继续
    if (!_accountStore.withdraw(userId, amount)) {
         _display.showError("Not enough balance");
         return;
    }


    // 发钞
    _cardDispenser.dispense(amount);
}


这里就随意写写, 有错误就别经结了
这里只考虑一台ATM, 你也能和面试官讨论如果有多个ATM的时候, 这些method要怎么设计比较好
下午面了四个managers还是跪了, 不知道标准为何




补充内容 (2018-11-6 18:27):
比较像是设计另外4个interface的API

"""


# *************************** 以下为可能的模板 ***************************
class Display:
    def read_input(self, display_text):
        pass

    def show_error(self, error_msg):
        pass

    def show_msg(self, msg):
        pass


class AccountStore:
    pass


class CardHandler:
    pass


class CashDispenser:
    pass


class CashIntake:
    pass


class ATM:
    def __init__(self):
        self._accountstore = AccountStore()
        self._cardhandler = CardHandler()
        self._cashdispenser = CashDispenser()
        self._cashintake = CashIntake()

    def menu(self, input):

        if input == "LOGIN":
            # TODO
            pass
        elif input == "CREATE_ACCOUNT":
            # TODO
            pass
        elif input == "WITHDRAW":
            # TODO
            pass
        elif input == "DEPOSIT":
            # TODO
            pass
        elif input == "CHECK_BALANCE":
            # TODO
            pass
        elif input == "LOGOUT":
            # TODO
            pass


# *************************** 以下为我的implementation ***************************
import random


class Display:
    def read_input(self, display_text):
        pass

    def show_error(self, error_msg):
        pass

    def show_msg(self, msg):
        pass


class AccountStore:
    ACCOUNT_ID_MAX = 999
    ACCOUNT_ID_MIN = 1

    def __init__(self):
        self._actid2pin = {}
        self._uid2actid = {}
        self._actid2blc = collections.defaultdict(int)
        self._lockedact = set()

    def login_verify_success(self, accountid, pin):
        if accountid not in self._actid2pin or self._actid2pin[accountid] != pin:
            return False
        if accountid in self._lockedact:
            return False
        return True

    def lock_account(self, accountid):
        self._lockedact.add(accountid)

    # return a valid account id if created
    def create_account(self, name, legal_id, pin):
        if legal_id in self._uid2actid:
            return -1
        account_id = self.generate_account_id(name)
        self._actid2pin[account_id] = pin
        self._uid2actid[legal_id] = account_id
        return account_id

    def generate_account_id(self, name):
        random.seed(name)
        account_id = random.randint(ACCOUNT_ID_MIN, ACCOUNT_ID_MAX)
        while account_id in self._actid2pin:
            account_id = random.randint(ACCOUNT_ID_MIN, ACCOUNT_ID_MAX)
        return account_id

    def check_balance(self, account_id):
        return self._actid2blc[account_id]

    def withdraw(self, account_id, amount):
        self._actid2blc[account_id] -= amount

    def deposit(self, account_id, amount):
        self._actid2blc[account_id] += amount


class CardHandler:
    # return None if no valid card; otherwise return card id
    def read_card(self):
        pass

    # spit out the physical card if any
    def spit_card(self):
        pass

    # create a new card for new account
    def create_card(self, account_id):
        pass


class CashDispenser:
    def __init__(self, atm):
        self._atm = atm

    def spit(self, amount):
        self._atm._cash -= amount


class CashIntake:
    def __init__(self, atm):
        self._atm = atm

    # return the amount intaken from cash/check deposit
    def intake(self):
        amount = self.detect_intake_amount()
        self._atm._cash += amount
        pass

    # return the amount intaken physically from cash/check deposit
    def detect_intake_amount(self):
        pass


class ATM:
    MAX_LOGIN_ATTEMPT = 5

    def __init__(self, cash):
        self._accountstore = AccountStore()
        self._cardhandler = CardHandler()
        self._cashdispenser = CashDispenser(self)
        self._cashintake = CashIntake(self)
        self._display = Display()

        self._session = None
        self._cash = cash

    def menu(self, input):
        if input == "LOGIN":
            self.login()
        elif input == "CREATE_ACCOUNT":
            self.create_account()
        elif input == "WITHDRAW":
            self.withdraw()
        elif input == "DEPOSIT":
            self.deposit()
        elif input == "CHECK_BALANCE":
            self.check_balance()
        elif input == "LOGOUT":
            self.logout()

    def login(self):
        # 0. check if there is no active session
        if self._session is not None:
            raise Exception(
                "Already in session - unexpected login during active session!"
            )

        # 1. read account id from valid card
        accountid = self._cardhandler.read_card()
        if accountid is None:
            self._display.show_error("Please insert a valid card.")
            return

        # 2. request pin code input
        pincode = self._display.read_input("Please enter your pin code.")
        failedcnt = 0

        # 3. verify pin code input and allow re-enter
        while (
            failedcnt < MAX_LOGIN_ATTEMPT
            and not self._accountstore.login_verify_success(accountid, pincode)
        ):
            failedcnt += 1
            pincode = self._display.read_input(
                "Incorrect Pin. Please enter your pin code again."
            )

        # 4. verify last entered, if valid then update session; otherwise, lock account
        if self._accountstore.login_verify_success(accountid, pincode):
            self._session = accountid

        else:
            self._display.show_error(
                "Too many failed attempt. Your account is locked. Please call 1-800-TWO-SIGM"
            )
            self._accountstore.lock_account(accountid)
            self._cardhandler.spit_card()

    def logout(self):
        if self._session is None:
            raise Exception("No active session - unexpected logout!")
        self._session = None

    def create_account(self):
        # 0. no active session
        if self._session is not None:
            raise Exception("Already in session - unexpected account creation request!")

        # 1. enter username, pin code
        username = self._display.read_input("Please enter your name.")
        legal_id = self._display.read_input("Please enter your DL id as legal id.")
        pincode = self._display.read_input("Please enter your pin code")
        pincode2 = self._display.read_input("Please verify your pin code")

        # 2. verify pincode input
        while pincode2 != pincode:
            pincode2 = self._display.read_input(
                "Second pin input doesn't match the first. Please try again."
            )

        # 3. create account if no account found for the given legal id
        account_id = self._accountstore.create_account(username, legal_id, pincode)
        if account_id == -1:
            self._display.show_error("User already exists. Account not created.")
        else:
            self._display.show_msg("Account created. Your account id is ", account_id)
            self._cardhandler.create_card(account_id)
            self._cardhandler.spit_card()

    def withdraw(self):
        # 0. validate session status
        if self._session is None:
            raise Exception("No active session - unexpected withdraw action!")

        # 1. ask for withdraw amount
        attempt_amount = self._display.read_input(
            "Please enter the amount you want to withdraw."
        )

        # 2. verify the balance with account store
        balance = self._accountstore.verify_balance(self._session)

        # 3. dispense only if both account and atm have enough balance
        if balance < attempt_amount:
            self._display.show_error("You don't have enough balance!")
        elif self._cash < attempt_amount:
            self._display.show_error("This ATM doesn't have enough cash!")
        else:
            self._cashdispenser.spit(attempt_amount)
            self._accountstore.withdraw(self._session, attempt_amount)

    def deposit(self):
        # 0. verify session status
        if self._session is None:
            raise Exception("No active session - unexpected deposit action!")

        # 1. ask for deposit
        self._display.show_msg("Please insert the cash or check to deposit.")
        amount = self._cashintake.intake()

        # 2. update account
        self._accountstore.deposit(self._session, amount)

        # 3. show message
        self._display.show_msg("Successfully deposit ", amount)

    def check_balance(self):
        # 0. verify session status
        if self._session is None:
            raise Exception("No active session - unexpected check balance action!")

        # 1. check balance
        amount = self._accountstore.check_balance(self._session)

        # 2. display balance
        self._display.show_msg("Your balance is ", amount)
