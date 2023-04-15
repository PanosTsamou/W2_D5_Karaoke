import unittest
from src.song import Song

class TestSong(unittest.TestCase):


    def setUp(self):
        self.sonng_1 = Song("Purple Haze", "Jimi Hendrix","Rock", 2.5)
        self.sonng_2 = Song("Whole Lotta Love", "Led Zeppelin","Rock", 3)

    def test_name_of_the_song1(self):
        self.assertEqual("Purple Haze", self.sonng_1.name)

    def test_artist_of_the_song1(self):
        self.assertEqual("Jimi Hendrix", self.sonng_1.artist)

    def test_gender_of_the_song1(self):
        self.assertEqual("Rock", self.sonng_1.gender)

    def test_duration_of_the_song1(self):
        self.assertEqual(2.5, self.sonng_1.duration)

    def test_name_of_the_song2(self):
        self.assertEqual("Whole Lotta Love", self.sonng_2.name)

    def test_artist_of_the_song2(self):
        self.assertEqual("Led Zeppelin", self.sonng_2.artist)

    def test_gender_of_the_song2(self):
        self.assertEqual("Rock", self.sonng_2.gender)

    def test_duration_of_the_song2(self):
        self.assertEqual(3, self.sonng_2.duration)