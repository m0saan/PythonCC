from LoginAttempts import User


class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges :")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """ An administrator is a special kind of user """

    def __init__(self, list_of_privilages):
        super().__init__('Admin', '', 21)
        self.list_of_privilages = list_of_privilages
        self.privilege = Privileges(list_of_privilages)
