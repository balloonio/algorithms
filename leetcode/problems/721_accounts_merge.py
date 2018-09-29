class Solution:
    def __init__(self):
        self.email2ids = collections.defaultdict(set)  # email : set of ids
        self.id2master = []  # id2master[i] = i's master id
        self.master2emails = collections.defaultdict(set)  # master id : set of emails

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.get_email_to_ids(accounts)
        self.id2master = [i for i in range(len(accounts))]

        for email, ids in self.email2ids.items():
            if len(ids) == 1:
                continue  # nothing to union
            masterid = None
            for accountid in ids:
                if masterid is None:
                    masterid = accountid
                    continue
                self.union(masterid, accountid)

        for accountid, account in enumerate(accounts):
            name, *emails = account
            master = self.find(accountid)
            self.master2emails[master].update(emails)

        result = []
        for master, emails in self.master2emails.items():
            emails = list(emails)
            emails.sort()
            name = accounts[master][0]
            result.append([name, *emails])
        return result

    def find(self, accountid):
        path = []
        while self.id2master[accountid] != accountid:
            path += [accountid]
            accountid = self.id2master[accountid]
        for account in path:
            self.id2master[account] = accountid
        return accountid

    def union(self, master, slave):
        if master == slave:
            return
        mfather = self.find(master)
        sfather = self.find(slave)
        self.id2master[sfather] = mfather

    def get_email_to_ids(self, accounts):
        for idx, account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                self.email2ids[email].add(idx)
        return


"""
What are we unioning? And based on what condition are we unioning?
We are unioning account id, or account index.
We are unioning two different account id whenever they share a same email
The best part is that, we dont need to union the emails within 1 account itself
"""
