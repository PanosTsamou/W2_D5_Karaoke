class Karaoke:
    
    def __init__(self, input_rooms, input_cash):
        self.all_rooms = input_rooms
        self.cash = input_cash
        self.rooms_occupied = []
        self.waiting_list = []

    def add_cash(self, amount):
        self.cash += amount

    def find_room_is_free(self, room):
        if room in self.rooms_occupied:
            return False
        else:
            return True

    
    def check_in(self, add_room , add_guest):
        if add_room.fee < add_guest.wallet and add_guest.age >= 18 and add_room.room_avaible and add_room not in self.rooms_occupied and add_room.check_if_they_fit(1):
            add_room.add_guests(add_guest)
            add_room.hours_occupied = add_guest.hours_to_stay
            self.rooms_occupied.append(add_room)
        elif add_room.fee < add_guest.wallet and add_guest.age >= 18 and add_room.room_avaible and add_room not in self.rooms_occupied and not add_room.check_if_they_fit(1):
            self.waiting_list.append(add_guest)
    
    def cheer_loudly(self, guest):
        for room in self.rooms_occupied:
            if guest in room.guests and room.free_songs.find_song_in_list(guest.pref_song):
                return "whooooo" 
        return "sorry"

        

    def check_out(self, guest):
        for room in self.rooms_occupied:
            if guest in room.guests:
                guest.decrease_monies(room.fee)
                room.room_clear()
                self.add_cash(room.fee)
                self.rooms_occupied.remove(room)

