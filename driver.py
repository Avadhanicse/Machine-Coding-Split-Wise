from controllers.bill_controller import BillController
from controllers.group_controller import GroupController
from controllers.user_controller import UserController

from services.bill_service import BillService
from services.group_service import GroupService
from services.user_service import UserService


userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('1','avadhani')
user2 = userController.addUser('2','ram')
print(user1)

members = [user1,user2]
grp1 = groupController.addGroup('gp1','kings',members)
print(grp1.getMembers())

paidBy={'user1':20,'user2':30}
contribution ={'user1':10,'user2':40}

bill=billController
bill.addBill('bil1','grp1',50,contribution,paidBy)
balance = billController.get_user_balance('user2')
print(balance)