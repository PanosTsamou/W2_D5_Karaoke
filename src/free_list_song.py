import csv

class FreeListSong:

    def __init__(self):
        self.free_song = []
        self.creat_the_list()

    def creat_the_list(self):
        with open('src/karafuncatalog.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                self.free_song.append(str(row[1]).title())

    def check_for_empty_list(self):
        if len(self.free_song) == 0:
            return True
        return False

    def find_song_in_list(self, song_to_find):
        if song_to_find in self.free_song:
            return True
        return False
    