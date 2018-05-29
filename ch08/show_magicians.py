# 8-9 Show Magicians


from ch08.magicians import show_magicians, return_great, make_great

names = ["William", "Bruce", "David", "Jackson"]
show_magicians(names)


print("\nReturn great ...")
show_magicians(return_great(names))
show_magicians(names)


print("\nMake great ....")
make_great(names)
show_magicians(names)



