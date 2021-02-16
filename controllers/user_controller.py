class UserController(object):
    def __init__(self, userService):
        self.userService = userService

    def addUser(self, id, name):
        service = self.userService
        return service.addUser(id,name)


