# 3-4 Invitation
# Invite somebody to join your dinner

names = ["Dog", "Cat", "Rabbit", "Duck"]
for name in names:
    print("Hello " + name + ", would you like to join my dinner?")

print()
print("Rabbit is sick, he can't join the dinner.\n")
names.remove("Rabbit")


print("May Frog can join the dinner.\n")
names.append("Frog")

for name in names:
    print("Hello " + name + ", would you like to join my dinner?")

print()
print("I found a bigger table, and I want to invite three more persons.\n")

names.insert(0, "Peiqi")
names.insert(3, "Qiaozhi")
names.append("Tutu")

for name in names:
    print("Hello " + name + ", would you like to join my dinner?")

print()
print("Sorry, I can't get the table on time. So I only can invite two persons to join my dinner.\n")

for name in names:
    print("Hi " + name + ", Sorry I can't invite you to join my dinner.")

print()

print("Hi " + names.pop(0) + ", Sorry I can't invite you to join my dinner.")
print("Hi " + names.pop(0) + ", Sorry I can't invite you to join my dinner.")
print("Hi " + names.pop(0) + ", Sorry I can't invite you to join my dinner.")
print("Hi " + names.pop(0) + ", Sorry I can't invite you to join my dinner.")
print("Hi " + names.pop(0) + ", Sorry I can't invite you to join my dinner.")


print()

for name in names:
    print("Hello " + name + ", would you like to join my dinner?")

del names[0]
del names[-1]

print()
print("Print the invitation list again.\n")

for name in names:
    print(name)




