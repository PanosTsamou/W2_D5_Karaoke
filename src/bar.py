class Bar:
    
    def __init__(self,input_cash):
        self.cash = input_cash
        self.tab_money = 0
        self.guests =[]
        self.guest_tab = {}
        self.bar_items = {
            "Drinks" : [{
                "name" : "Gin And Tonic",
                "price" : 5,
                "age_limit" : True
            },
            {
                "name" : "Vodca",
                "price" : 7,
                "age_limit" :True
            },
            {
               "name" : "Tequila",
               "price" : 6,
               "age_limit" : True
            },
            {
                "name" : "Joker IPA",
                "price" : 3,
                "age_limit" : True
            },
            {
                "name" : "Brewdog AF",
                "price" : 3,
                "age_limit" : False
            }   
            ],
            "Soft Drinks": [
                {
                    "name" : "Diet Coke",
                    "price" : 2,
                    "age_limit" : False
                },
                {
                    "name" : "Coke",
                    "price" : 2,
                    "age_limit" : False
                },
                {
                    "name" : "Lemonade",
                    "price" : 2,
                    "age_limit" : False
                },
                {
                    "name" : "Irn Bru",
                    "price" : 3,
                    "age_limit" : False
                }
            ],
            "Food" :[
                {
                    "name" : "Cheeseburger",
                    "price" : 10,
                    "age_limit" : False
                },
                {
                    "name" : "Burger",
                    "price" : 8,
                    "age_limit" : False
                },
                {
                    "name" : "Chips",
                    "price" : 6,
                    "age_limit" : False
                },
                {
                    "name" : "Falafel Wrap",
                    "price" : 8,
                    "age_limit" : False
                }
            ],
            "Sweets" : [
                {
                    "name" : "Haribo",
                    "price" : 1,
                    "age_limit" : False
                },
                {
                    "name" : "Galaxy Bar",
                    "price" : 1,
                    "age_limit" : False
                },
                {
                    "name" : "Marshmallow",
                    "price" : 2,
                    "age_limit" : False
                },
                {
                    "name" : "Brownie",
                    "price" : 5,
                    "age_limit" : False
                }
            ]
        }

    def add_monies(self, amount):
        self.cash += amount

    def add_guest_in_the_bar(self, add_guest):
        self.guests.append(add_guest)

    def remove_from_the_bar(self, remove_guest):
        self.guests.remove(remove_guest)

    def find_item_in_list(self, searching_item):
        for pref in self.bar_items:
            for item in self.bar_items[pref]:
                if item["name"] == searching_item:
                    return item


    def serve_guest(self, serve_guest):
        total_amount = 0
        if serve_guest in self.guests:
            for pref in serve_guest.preferences:
                item = self.find_item_in_list(pref)
                if item is not None and item["age_limit"] and serve_guest.age >= 18:
                    total_amount += item["price"]
                elif item is not None and not item["age_limit"]:
                    total_amount += item["price"]
        if total_amount <= serve_guest.wallet:
            serve_guest.decrease_monies(total_amount)
            self.add_monies(total_amount)
        self.remove_from_the_bar(serve_guest)


    def add_items_in_tab_and_increase_money(self, guest_open_tab):
        self.guest_tab[guest_open_tab.name] ={}
        self.guest_tab[guest_open_tab.name]["tab_items"] = [] 
        self.guest_tab[guest_open_tab.name]["tab_money"] =  0
        self.guest_tab[guest_open_tab.name]["location"] =  ""
        if guest_open_tab in self.guests:
            self.guest_tab[guest_open_tab.name]["location"] =  "Bar"
            for pref in guest_open_tab.preferences:
                item = self.find_item_in_list(pref)
                if item is not None and item not in self.guest_tab[guest_open_tab.name]["tab_items"] and item["age_limit"] and guest_open_tab.age >= 18:
                    self.guest_tab[guest_open_tab.name]["tab_items"].append(item["name"]) 
                    self.guest_tab[guest_open_tab.name]["tab_money"] +=  item["price"]
                    
                elif item is not None and item not in self.guest_tab[guest_open_tab.name]["tab_items"] and not item["age_limit"]:
                    self.guest_tab[guest_open_tab.name]["tab_items"].append(item["name"]) 
                    self.guest_tab[guest_open_tab.name]["tab_money"] +=  item["price"]
        else: 
            self.guest_tab[guest_open_tab.name]["location"] =  "Room"
            for pref in guest_open_tab.preferences:
                item = self.find_item_in_list(pref)
                if item is not None and item not in self.guest_tab[guest_open_tab.name]["tab_items"] and item["age_limit"] and guest_open_tab.age >= 18:
                    self.guest_tab[guest_open_tab.name]["tab_items"].append(item["name"]) 
                    self.guest_tab[guest_open_tab.name]["tab_money"] +=  item["price"]
                    
                elif item is not None and item not in self.guest_tab[guest_open_tab.name]["tab_items"] and not item["age_limit"]:
                    self.guest_tab[guest_open_tab.name]["tab_items"].append(item["name"]) 
                    self.guest_tab[guest_open_tab.name]["tab_money"] +=  item["price"]
            
        
        # if self.guest_tab[guest_open_tab.name]["tab_money"] == 0:
        #     del(self.guest_tab[guest_open_tab.name])   
        #     if guest_open_tab in self.guests:
        #         self.guests.remove(guest_open_tab)         
            
    def pay_for_bar_tab(self, guest_is_paying):
        for guest_name in self.guest_tab.keys():
            if guest_name == guest_is_paying.name and guest_is_paying in self.guests:
                guest_is_paying.decrease_monies(self.guest_tab[guest_name]["tab_money"])
                self.add_monies(self.guest_tab[guest_name]["tab_money"])
                del(self.guest_tab[guest_is_paying.name])   
                self.guests.remove(guest_is_paying)
                break 
            else:
                results = self.guest_tab[guest_name]["tab_money"]
                del(self.guest_tab[guest_is_paying.name])   
                return results
                

            