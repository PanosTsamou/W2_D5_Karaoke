import unittest
from src.bar import Bar
from src.guests.guest import Guest

class TestBar(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Paul", 32, 40, "Purple Haze", 2)
        self.bar = Bar(1200)

    def test_bar_items(self):
        self.assertEqual(5,len(self.bar.bar_items["Drinks"]))
        self.assertEqual(4,len(self.bar.bar_items))

    def test_cash(self):
        self.assertEqual(1200,self.bar.cash)

    def test_adding_monies(self):
        self.bar.add_monies(200)
        self.assertEqual(1400,self.bar.cash)

    def test_add_guest_in_the_bar(self):
        self.bar.add_guest_in_the_bar(self.guest_1)
        self.assertEqual(1,len(self.bar.guests))

    def test_find_item_in_list(self):
        self.item = self.bar.find_item_in_list("Diet Coke")
        self.assertEqual("Diet Coke",self.item["name"])

    def test_serve_guest_in_the_bar(self):
        self.guest_1.add_preferences(["Vodca","Coke","Cheeseburger"])
        self.bar.add_guest_in_the_bar(self.guest_1)
        self.bar.serve_guest(self.guest_1)
        self.assertEqual(21,self.guest_1.wallet)
        self.assertEqual(1219,self.bar.cash)

    def test_if_the_bar_can_hold_tab(self):
        self.guest_1.add_preferences(["Vodca","Coke","Cheeseburger"])
        self.bar.add_guest_in_the_bar(self.guest_1)
        self.bar.add_items_in_tab_and_increase_money(self.guest_1)
        self.guest_1.add_preferences("Galaxy Bar")
        self.bar.add_items_in_tab_and_increase_money(self.guest_1)
        self.assertEqual(4,len(self.bar.guest_tab[self.guest_1.name]["tab_items"]))  
        self.assertEqual(20,self.bar.guest_tab[self.guest_1.name]["tab_money"])
        self.assertEqual("Bar",self.bar.guest_tab[self.guest_1.name]["location"])

    def test_pay_the_bar_tab(self):
        self.guest_1.add_preferences(["Vodca","Coke","Cheeseburger"])
        self.bar.add_guest_in_the_bar(self.guest_1)
        self.bar.add_items_in_tab_and_increase_money(self.guest_1)
        self.bar.pay_for_bar_tab(self.guest_1)
        self.assertEqual(0,len(self.bar.guest_tab))  
        self.assertEqual(1219,self.bar.cash)
        self.assertEqual(21,self.guest_1.wallet)
        self.assertEqual(0,len(self.bar.guests))

