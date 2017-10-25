class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Zum Geburtstag viel Gluck",
                   "Zum Geburtstag viel Gluck",
                   "Zum Geburtstab alles Gute",
                   "Zum Geburtstag viel Gluck"])

bulls_on_parade = Song(["They rally around tha family",
                        "With a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
