def make_album(artist, album, songs=None):
    print(f'Playing "{album.title()}" ({songs} songs): by {artist.title()}')
    if songs:
        music = {
            'Artist': artist,
            'Album': album,
            'Songs': songs
        }
    else:
        music = {
            'Artist': artist,
            'Album': album
        }
    print(music)


make_album('Snoop', 'Sometihng with weed')
make_album('Weezer', 'Teal Album')
make_album(input("\nArtist: "), input("Album: "), input("Number of songs: "))
