import unittest
from src.guests.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Paul", 32, 40, "Purple Haze", 2)
        self.guest_2 = Guest("Dave", 23, 20, "Whole Lotta Love", 1)
        
    def test_name_of_guest1(self):
        self.assertEqual("Paul", self.guest_1.name)

    def test_age_of_guest1(self):
        self.assertEqual(32, self.guest_1.age)

    def test_money_of_guest1(self):
        self.assertEqual(40, self.guest_1.wallet)
    
    def test_song_to_listen_of_guest1(self):
        self.assertEqual("Purple Haze", self.guest_1.pref_song)

    def test_of_hours_to_stay_guest1(self):
        self.assertEqual(2,self.guest_1.hours_to_stay)

    def test_reduce_money_guest1(self):
        self.guest_1.decrease_monies(5)
        self.assertEqual(35,self.guest_1.wallet)

    def test_name_of_guest2(self):
        self.assertEqual("Dave", self.guest_2.name)

    def test_age_of_guest2(self):
        self.assertEqual(23, self.guest_2.age)

    def test_money_of_guest2(self):
        self.assertEqual(20, self.guest_2.wallet)
    
    def test_song_to_listen_of_guest2(self):
        self.assertEqual("Whole Lotta Love", self.guest_2.pref_song)

    def test_of_hours_to_stay_guest2(self):
        self.assertEqual(1,self.guest_2.hours_to_stay)

    def test_reduce_money_guest2(self):
        self.guest_2.decrease_monies(7)
        self.assertEqual(13,self.guest_2.wallet)