import unittest
from src.karaoke import Karaoke
from src.guests.guest import Guest
from src.room import Room
from src.songs.free_list_song import FreeListSong
from src.guests.booking_room import BookingRoom
from src.bar import Bar

class KaraokeTest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Paul", 32, 100, "Dog Eat Dog", 2)
        self.guest_2 = Guest("Dave", 15, 20, "Purple Haze", 1)
        self.free_song = FreeListSong()
        self.bar = Bar(300)
        self.room_1 = Room("A22", 2, 20, self.free_song)
        self.room_2 = Room("A23", 5, 40, self.free_song)
        self.room_3 = Room("A24", 3, 25, self.free_song)
        self.booking_guest_1 = BookingRoom(self.guest_1, 3)
        self.booking_guest_2 = BookingRoom(self.guest_2, 1)
        self.karaoke_venue = Karaoke([self.room_1, self.room_2, self.room_3], 800, self.bar)

    def test_check_in_guest1(self):
        self.karaoke_venue.check_in(self.room_2, self.booking_guest_1)
        self.assertEqual(1, len(self.room_2.guests))
        self.assertEqual(1, len(self.room_2.guest_songs))
        self.assertEqual(1,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(2,self.room_2.hours_occupied)

    def test_check_in_guest1_wrong_room(self):
        self.karaoke_venue.check_in_with_search(self.room_1, self.booking_guest_1)
        self.assertEqual(1, len(self.room_3.guests))
        self.assertEqual(1, len(self.room_3.guest_songs))
        self.assertEqual(1,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(2,self.room_3.hours_occupied)

    def test_cheering(self):
        self.karaoke_venue.check_in(self.room_2,self.booking_guest_1)
        cheering = self.karaoke_venue.cheer_loudly(self.booking_guest_1)
        self.assertEqual("whooooo",cheering)

    def test_check_in_guest2(self):
        self.karaoke_venue.check_in(self.room_1, self.booking_guest_2)
        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(0, len(self.room_1.guest_songs))
        self.assertEqual(0,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(0,self.room_1.hours_occupied)

    def test_check_out_guest1(self):
        self.karaoke_venue.check_in(self.room_2, self.booking_guest_1)
        self.karaoke_venue.check_out(self.booking_guest_1)
        self.assertEqual(60,self.booking_guest_1.guest.wallet)
        self.assertEqual(0, len(self.room_2.guests))
        self.assertEqual(0, len(self.room_2.guest_songs))
        self.assertEqual(840, self.karaoke_venue.cash)
        self.assertEqual(0,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(0,self.room_2.hours_occupied)

    def test_room_tab(self):
        self.booking_guest_1.guest.add_preferences(["Vodca","Coke","Cheeseburger"])
        self.karaoke_venue.check_in_with_search(self.room_1, self.booking_guest_1)
        self.assertEqual(1, len(self.room_3.guests))
        self.assertEqual(1, len(self.room_3.guest_songs))
        self.assertEqual(1,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(2,self.room_3.hours_occupied)
        self.assertEqual(3,len(self.bar.guest_tab[self.guest_1.name]["tab_items"]))  
        self.assertEqual(19,self.bar.guest_tab[self.guest_1.name]["tab_money"])
        self.assertEqual("Room",self.bar.guest_tab[self.guest_1.name]["location"])

    def test_check_out_with_tab_guest1(self):
        self.booking_guest_1.guest.add_preferences(["Vodca","Coke","Cheeseburger"])
        self.karaoke_venue.check_in_with_search(self.room_2, self.booking_guest_1)
        self.karaoke_venue.check_out_with_tab (self.booking_guest_1)
        self.assertEqual(41,self.booking_guest_1.guest.wallet)
        self.assertEqual(0, len(self.room_2.guests))
        self.assertEqual(0, len(self.room_2.guest_songs))
        self.assertEqual(840, self.karaoke_venue.cash)
        self.assertEqual(0,len(self.karaoke_venue.rooms_occupied))
        self.assertEqual(0,self.room_2.hours_occupied)
        self.assertEqual(0,len(self.bar.guest_tab))  
        self.assertEqual(319,self.bar.cash)
        self.assertEqual(0,len(self.bar.guests))
        