# 8-9 Show Magicians


import ch08.magicians as mag

names = ["William", "Bruce", "David", "Jackson"]
mag.show_magicians(names)


print("\nReturn great ...")
mag.show_magicians(mag.return_great(names))
mag.show_magicians(names)


print("\nMake great ....")
mag.make_great(names)
mag.show_magicians(names)



