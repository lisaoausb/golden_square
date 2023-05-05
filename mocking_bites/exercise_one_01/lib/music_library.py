class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.list_tracks = []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        self.list_tracks.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        self.matching_tracks = []
        for track in self.list_tracks:
            if track.matches(keyword) == True:
                self.matching_tracks.append(track)
        return self.matching_tracks