from services.bill_service_interface import BillServiceInterface
from models.bill import Bill


class BillService(BillServiceInterface):
    billDetails = {}

    def addBill(self, id, groupId, amount, contribution, paidBy):
        bill = Bill()
        bill.setId(id)
        bill.setGroupid(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidby(paidBy)
        self.__class__.billDetails[id] = bill
        return bill
