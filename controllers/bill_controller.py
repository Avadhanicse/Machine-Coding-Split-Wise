class BillController(object):
    def __init__(self, billService):
        self.billService = billService

    def addBill(self, id, groupId, amount, contribution, paidBy):
        return self.billService.addBill(id, groupId, amount, contribution, paidBy)

    def get_user_balance(self, userId):
        balance = 0
        for bilId in self.billService.billDetails:
            bill = self.billService.billDetails.get(bilId)
            if userId in bill.getContribution():
                balance -= bill.getContribution().get(userId)
            if userId in bill.getPaidby():
                balance+=bill.getPaidby().get(userId)
        return balance
