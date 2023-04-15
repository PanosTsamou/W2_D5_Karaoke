class Room:
    
    def __init__(self, input_name, input_room_capacity, input_fee, input_free_songs):
        self.guests = []
        self.guest_songs = []
        self.hours_occupied = 0
        self.name = input_name
        self.free_songs = input_free_songs
        self.room_capacity = input_room_capacity
        self.fee = input_fee

    def check_availability(self):
        if len(self.guests) == 0:
            return True
        
        else:
            return False

    def add_guests(self, new_guest):
        self.guests.append(new_guest)
        self.guest_songs.append(new_guest.pref_song)
        if self.hours_occupied < new_guest.hours_to_stay:
            self.hours_occupied = new_guest.hours_to_stay


    # def remove_guests(self, remove_guest):
    #     self.guests.remove(remove_guest)

    # def initialise_hours(self, hours):
    #     if self.hours_occupied < hours:
    #         self.hours_occupied = hours

    def room_clear(self):
        self.hours_occupied = 0
        self.guests = []
        self.guest_songs = []

    