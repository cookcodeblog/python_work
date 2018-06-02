from ch09.user import User
from ch09.user import Admin
from ch09.privileges import Privileges

william = User("William", "Lin", "m")
william.describe_user()
william.greet_user()
print()

lily = User("Lily", "Zhu", "Female")
lily.describe_user()
lily.greet_user()
print()

lily.last_name = "Wei"
lily.describe_user()
print()

print("----------------------------------------------------")

lilei = User("lilei", "liu", "m")
lilei.describe_user()
lilei.increment_login_attempts(1)
lilei.describe_user()
lilei.increment_login_attempts(2)
lilei.describe_user()
lilei.reset_login_attemps()
lilei.describe_user()

print()

privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin = Admin("Gugu", "Liu", "m", privileges)
admin.describe_user()
privileges.show_privileges()


