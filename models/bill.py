class Bill(object):
    def __init__(self):
        self.id = None
        self.groupid = None
        self.amount = None
        self.contribution = {}
        self.paidby = {}

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setGroupid(self, groupid):
        self.groupid = groupid

    def getGroupid(self):
        return self.groupid

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setContribution(self, contribution):
        self.contribution = contribution

    def getContribution(self):
        return self.contribution

    def setPaidby(self, paidby):
        self.paidby = paidby

    def getPaidby(self):
        return self.paidby
