from abc import ABC, abstractmethod


class BillServiceInterface(ABC):
    @abstractmethod
    def addBill(self, id, groupId, amount, contribution, paidBy):
        pass
