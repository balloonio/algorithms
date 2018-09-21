class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def __init__(self):
        self.email2master_email = {}
        self.email2id = {}

    def accountsMerge(self, accounts):
        # write your code here
        if not accounts:
            return []

        # initialize so that every email is pointing to they current appearing index as father
        for account_id, account in enumerate(accounts):
            if not account:
                continue  # blank account if there is
            name, *emails = account
            for email in emails:
                self.email2master_email[email] = email
                self.email2id[email] = account_id

        for account_id, account in enumerate(accounts):
            if not account:
                continue  # blank account if there is
            name, *emails = account
            for email in emails:
                self.union(emails[0], email)
        print(self.email2master_email)

        result = collections.defaultdict(list)
        for email, master_email in self.email2master_email.items():
            master_email = self.find(email)
            account = accounts[self.email2id[master_email]]
            name = account[0]
            result[master_email].append(email)

        final_result = []
        for master_email, email_list in result.items():
            account = accounts[self.email2id[master_email]]
            name = account[0]
            email_list.sort()
            email_list.insert(0, name)
            final_result.append(email_list)

        return final_result

    def union(self, email1, email2):

        father1 = self.find(email1)
        father2 = self.find(email2)

        self.email2master_email[father2] = father1
        return

    def find(self, email):
        path = []
        while self.email2master_email[email] != email:
            path.append(email)
            email = self.email2master_email[email]

        for p in path:
            self.email2master_email[p] = email

        return email
