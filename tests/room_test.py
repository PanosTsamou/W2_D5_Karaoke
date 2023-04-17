import unittest
from src.room import  Room
from src.guests.guest import Guest

class TestRoom(unittest.TestCase):
    

    def setUp(self):
        self.room_1 = Room("A22", 2, 25, "Purple Haze")
        self.guest_1 = Guest("Dave", 30, 50, "Whole Lotta Love", 2)
    
    def test_name_of_the_room(self):
        self.assertEqual("A22", self.room_1.name)

    def test_capacity_of_the_room(self):
        self.assertEqual(2, self.room_1.room_capacity)

    def test_room_fee(self):
        self.assertEqual(25, self.room_1.fee)

    def test_room_song(self):
        self.assertEqual("Purple Haze", self.room_1.free_songs)
    
    def test_free_room(self):
        self.assertEqual(True,self.room_1.room_avaible)

    def test_if_the_group_fit_in_room(self):
        self.assertEqual(True,self.room_1.check_if_they_fit(2))

    def test_add_gust_in_the_room(self):
        self.room_1.add_guests(self.guest_1)
        self.assertEqual(False, self.room_1.room_avaible)
        self.assertEqual(1, len(self.room_1.guests))
        self.assertEqual(1, len(self.room_1.guest_songs))
        self.assertEqual(2, self.room_1.hours_occupied)
        
    def test_clear_the_room(self):
        self.room_1.add_guests(self.guest_1)
        self.room_1.room_clear()
        self.assertEqual(True, self.room_1.room_avaible)
        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(0, len(self.room_1.guest_songs))
        self.assertEqual(0, self.room_1.hours_occupied)


