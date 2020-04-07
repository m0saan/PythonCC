def make_album(artist_name, album_title, number_of_tracks=0):
    _di_ct = {'name': artist_name, 'album name': album_title, }
    if number_of_tracks:
        _di_ct['number of tracks'] = number_of_tracks
    return _di_ct


# print(make_album('linkin park', 'Living things'))
# print(make_album('eminem', 'Kamikasi'))
# print(make_album('Youness', 'Louad', 13))
