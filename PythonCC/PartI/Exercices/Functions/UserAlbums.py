import Album

while True:
    artist_name = input("Enter the name of the artist or 'q' to quit : ")
    if artist_name == 'q':
        break
    album_name = input("Enter the name of the album : ")

    print(Album.make_album(artist_name, album_name))
