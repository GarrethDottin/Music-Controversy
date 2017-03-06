globalVar = {}

def artistRateOfChangePerAlbum(timestamp, artist,album,  score):
    if bool(artist in globalVar) == False:
        globalVar[artist] = {}
        globalVar[artist][album] = {}
        globalVar[artist][album]['rateOfChangeScore'] = 0
        globalVar[artist][album]['timestamp'] = timestamp
        globalVar[artist]['previousAlbumScore'] = score
    else:
        globalVar[artist][album] = {}
        latestAlbumScoreChange = score - globalVar[artist]['previousAlbumScore']
        globalVar[artist][album]['rateOfChangeScore'] = latestAlbumScoreChange
        globalVar[artist][album]['timestamp'] = timestamp
        globalVar[artist]['previousAlbumScore'] = score
        print globalVar

