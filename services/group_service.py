from services.group_service_interface import GroupServiceInterface
from models.groups import Groups


class GroupService(GroupServiceInterface):
    def addGroup(self,id,name,members):
        group = Groups()
        group.setId(id)
        group.setName(name)
        group.setMembers(members)
        return group
