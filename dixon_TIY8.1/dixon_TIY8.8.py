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


flag = True
while flag == True:
    response = input("Would you like to make an album? Yes/No ")
    if response == 'no' or 'NO' or 'nO' or 'No':
        flag = False
    if response != 'no' or 'NO' or 'nO' or 'No':
        artist_input = input("\nEnter Artist: ")
        album_input = input("Enter Album: ")
        song_input = input("Enter the number of songs: ")
        make_album(artist_input, album_input, song_input)
