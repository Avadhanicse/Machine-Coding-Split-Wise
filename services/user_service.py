from services.user_service_interface import UserServiceInterface
from models.users import User


class UserService(UserServiceInterface):
    def addUser(self,id, name):
        user = User()
        user.setId(id)
        user.setName(name)
        return user
