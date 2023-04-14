class Guest():

    def __init__(self, input_name, input_age, input_wallet, input_pref_song, input_hours_to_stay):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
        self.pref_song = input_pref_song
        self.hours_to_stay = input_hours_to_stay

    def decrease_monies(self,amount):
        self.wallet -= amount

        
