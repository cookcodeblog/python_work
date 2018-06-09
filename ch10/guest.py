# 10-3 Guest

# name = input("What is your name please ? ")
# # Don't forget add "w" to identify you want to write sth into the file
# with open("guest.txt", "w") as file_obj:
#     file_obj.write(name)


with open("guest.txt", "a") as file_obj:
    while True:
        name = input("What is your name please? ")
        file_obj.write(name + "\n")
        repeat = input("Add other guest? (yes / no) ")
        if repeat.lower() == "no":
            break
