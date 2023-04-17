class Guest():

    def __init__(self, input_name, input_age, input_wallet, input_pref_song, input_hours_to_stay):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
        self.pref_song = input_pref_song
        self.hours_to_stay = input_hours_to_stay
        self.preferences = []

    def decrease_monies(self, amount):
        self.wallet -= amount

        
    def add_preferences(self, preferred_item):
        if isinstance(preferred_item, str):
            self.preferences.append(preferred_item)
        else:
            for item in preferred_item:
                self.preferences.append(item)
