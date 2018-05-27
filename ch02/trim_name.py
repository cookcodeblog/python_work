# 2-7 Trim whitespace in name
# Store a name, and add some white sapces (e.g. ' ', '\t', '\n')
# And use lstrip(), rstrip() and strip() method to remove the white spaces

# ends with one space
name = "William "
print("==" + name.lstrip() + "==")
print("==" + name.rstrip() + "==")
print("==" + name.strip() + "==")
print("---------------------------")

# ends with two spaces
name = "William  "
print("==" + name.lstrip() + "==")
print("==" + name.rstrip() + "==")
print("==" + name.strip() + "==")
print("---------------------------")

# starts/ends with two spaces
name = "  William  "
print("==" + name.lstrip() + "==")
print("==" + name.rstrip() + "==")
print("==" + name.strip() + "==")
print("---------------------------")


# starts with two spaces, and ends with two '\t'
name = "  William\t\t"
print("==" + name.lstrip() + "==")
print("==" + name.rstrip() + "==")
print("==" + name.strip() + "==")
print("---------------------------")

# starts with two spaces, and ends with two '\n'
name = "  William\n\n"
print("==" + name.lstrip() + "==")
print("==" + name.rstrip() + "==")
print("==" + name.strip() + "==")
print("---------------------------")