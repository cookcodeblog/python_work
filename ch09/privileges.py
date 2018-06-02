# 9-8 Privileges


class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Has privileges:")
        for privilege in self.privileges:
            print(privilege)\
