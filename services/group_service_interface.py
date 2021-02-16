from abc import ABC, abstractmethod


class GroupServiceInterface(ABC):
    @abstractmethod
    def addGroup(self, id, name, members):
        pass
