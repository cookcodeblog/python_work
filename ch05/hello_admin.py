# 5-8 Say something special to Admin

names = ["William", "Tome", "Peiqi", "Admin", "Sky"]

for name in names:
    if name == "Admin":
        print("hello " + name + ", would you like to see a status report?")
    else:
        print("Hello " + name + ", thank you for logging in again.")

print()
print("Given an empty name list\n")
names = []
if names:
    for name in names:
        if name == "Admin":
            print("hello " + name + ", would you like to see a status report?")
        else:
            print("Hello " + name + ", thank you for logging in again.")
else:
    print("We need find some users!")

if not names:
    print("Let us find some users!")
