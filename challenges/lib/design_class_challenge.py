class MusicTracker:
    # None

    def __init__(self):
        # Parameters: none
        # Side effects: keeps a list of songs that will be added to
        self.songs = [] 

    def add_song(self, song):
        if song == "":
            raise Exception("Song cannot be empty")
        else:
            self.songs.append(song)
        # Parameters: takes a song I have listened to, string
        # Returns: nothing
        # Side effects: adds to the list in the initialiser
        # throws an error if string is empty

    def see_list(self):
        # Parameters: none
        # Returns: list of songs
        # Side effects: throws an error if list is empty
        if len(self.songs) == 0:
            raise Exception('You have not listened to any songs')
        else:
            return self.songs