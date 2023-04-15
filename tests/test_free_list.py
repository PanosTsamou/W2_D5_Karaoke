import unittest
from src.free_list_song import FreeListSong

class TestFreeListSong(unittest.TestCase):

    def setUp(self):
        self.free_list_of_song = FreeListSong()

    def test_list_empty(self):
        self.assertEqual(False,self.free_list_of_song.check_for_empty_list())

    def test_find_song_in_list(self):
        self.assertEqual(True,self.free_list_of_song.find_song_in_list("Come Fly With Me"))