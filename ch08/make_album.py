# 8-7 make_album() function


# be care of the variable life cycle
# function inner can see the outer variable. it is danger.
# try to use another name to avoid this duplication, e.g. _<name>
def make_album(_singer, _album_name, _song_count=0):
    """Make an album"""
    _album = {'singer': singer, 'album_name': _album_name}
    if _song_count:
        _album['song_count'] = _song_count
    return _album


print(make_album("Jack Zhou", "Flowers"))
print(make_album("Qiqi Wen", "Youth Times", 8))
print()

while True:
    singer = input("Please input a signer's name: ")
    album_name = input("Please input an album name: ")
    album = make_album(singer, album_name)
    print("Made an album: " + str(album))
    repeat = input("\nContinue? (yes / no) ")
    if repeat.lower() == "no":
        break



