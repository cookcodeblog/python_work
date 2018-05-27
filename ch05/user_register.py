# 5-10 Check User Names

current_users = ["William", "Tome", "Peiqi", "Admin", "Sky"]
new_users = ["tome", "Lily"]

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print("User name already exist: " + new_user + ", please try another name.")
    else:
        print("Name is available to register: " + new_user)
