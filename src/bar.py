class Bar:
    
    def __init__(self,input_cash):
        self.cash = input_cash
        self.tab_money = 0
        self.tab_items = []
        self.guests = []
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
               "name" : "Tecila",
               "price" : 6,
               "age_limit" : True
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
                    "price" : 1.5,
                    "age_limit" : False
                },
                {
                    "name" : "Marshmallow",
                    "price" : 2,
                    "age_limit" : False
                },
                {
                     "name" : "Browny",
               "price" : 6,
               "age_limit" : True
                }
            ]
        }