import unittest
from src.karaoke import Karaoke
from src.guest import Guest
from src.room import Room

class KaraokeTest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Paul", 32, 40, "Purple Haze", 2)
        self.guest_2 = Guest("Dave", 23, 20, "Whole Lotta Love", 1)
        self.room_1 = Room("A22", 2, 25, "Purple Haze")
        self.room_2 = Room("A23", 5, 40, "Whole Lotta Love")
        self.karaoke_venue = Karaoke([self.room_1, self.room_2], 800)

    def test_check_in_guest1(self):
        self.karaoke_venue.check_in(self.room_1, self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))
        self.assertEqual(1, len(self.room_1.guest_songs))
        self.assertEqual(1,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(2,self.room_1.hours_occupied)

    def test_check_in_guest2(self):
        self.karaoke_venue.check_in(self.room_1, self.guest_2)
        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(0, len(self.room_1.guest_songs))
        self.assertEqual(0,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(0,self.room_1.hours_occupied)

    def test_check_out_guest1(self):
        self.karaoke_venue.check_in(self.room_1, self.guest_1)
        self.karaoke_venue.check_out(self.guest_1)
        self.assertEqual(15,self.guest_1.wallet)
        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(0, len(self.room_1.guest_songs))
        self.assertEqual(825, self.karaoke_venue.cash)
        self.assertEqual(0,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(0,self.room_1.hours_occupied)