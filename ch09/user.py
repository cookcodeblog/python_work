# 9-3 User


class User:

    def __init__(self, first_name, last_name, gender, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print("Name: " + str(self.first_name).title() + " " + str(self.last_name).title())
        print("Gender: " + str(self.gender))
        print("Login attempts: " + str(self.login_attempts))

    def greet_user(self):
        name = str(self.first_name).title() + " " + str(self.last_name).title()
        if str(self.gender).lower() in ("m", "male"):
            name = "Mr. " + name
        else:
            name = "Mrs. " + name

        print("Hi " + name + ".")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attemps(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, gender, privileges, login_attempts=0):
        super().__init__(first_name, last_name, gender, login_attempts)
        self.privileges = privileges
