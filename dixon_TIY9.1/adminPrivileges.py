from justUsers import User


class Admin(User):
    def show_privileges(self):
        show = Privileges()
        show.show_privilege()


class Privileges:
    def __init__(self):
        self.privileges = ['add post = True', 'delete post = True', 'ban user = True']

    def show_privilege(self):
        for privilege in self.privileges:
            print(privilege)


