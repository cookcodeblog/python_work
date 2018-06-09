# 10-1 Learn Python


# Print file content
with open("learning_python.txt") as file_obj:
    file_content = file_obj.read()
    print(file_content.rstrip())

print()

# Print line by line
with open("learning_python.txt") as file_obj:
    for line in file_obj.readlines():
        print(line.rstrip())

print()

# Put file contents to a list, and print the list
with open("learning_python.txt") as file_obj:
    contents = []
    for line in file_obj.readlines():
        contents.append(line.rstrip())
    for line in contents:
        print(line)

print()


# Learn C programming language
with open("learning_python.txt") as file_obj:
    for line in file_obj.readlines():
        line = line.replace("Python", "C")
        print(line.rstrip())
