# Magicians Module


def show_magicians(names):
    """Print each item"""
    for name in names:
        print(name)


def make_great(names):
    """Modify each item in original list"""
    for i, item in enumerate(names):
        names[i] = "The great " + names[i]


def return_great(names):
    """Return a new list without mofidying original lsit"""
    return ["The great " + name for name in names]




