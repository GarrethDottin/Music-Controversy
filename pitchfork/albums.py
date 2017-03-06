import pitchfork
import artistAnalysis
import unicodedata


listOfArtists = ['Kanye West']




for artist in listOfArtists:
    artistDetails = {}
    artistDetails["artist"] = artist;
    individualArtistAlbums = pitchfork.allAlbums(artist)[::-1]
    for album in individualArtistAlbums:
        albumTitle = unicodedata.normalize('NFKD', album).encode('ascii', 'ignore')
        albumDetails = pitchfork.search(artist, albumTitle)
        if hasattr(albumDetails, 'score') == True:
            artistAnalysis.artistRateOfChangePerAlbum(albumDetails.timestamp,  artist,albumTitle, albumDetails.score())

    # Create a spreadsheet with all artists
    # Controversy and non controversial point
    # Read the spreadsheet and run through Python
    # Check from Pitchfork
    # Analyze if they have a change in controversy after controversy point
    # Analyze if they have a long term drop
    # Save entire artist with Album to Database


    #Lingering Questions
        # How do I determine if someone is controversial
        #