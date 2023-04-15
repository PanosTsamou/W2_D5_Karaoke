class Karaoke:
    
    def __init__(self, input_rooms, input_cash):
        self.all_rooms = input_rooms
        self.cash = input_cash
        self.rooms_occupied = []

    def add_cash(self, amount):
        self.cash += amount

    def find_room_is_free(self, room):
        if room in self.rooms_occupied:
            return False
        else:
            return True

    
    def check_in(self, add_room , add_guest):
        if add_room.fee < add_guest.wallet and add_guest.age >= 18 and add_room.check_availability() and add_room not in self.rooms_occupied:
            add_room.add_guest(add_guest)
            self.room.occupied = self.guest.hours_to_stay
            self.rooms_occupied.append(add_room)

        

    def check_out(self, guest):
        for room in self.rooms_occupied:
            if guest in room.guest:
                guest.decrease_monies(room.fee)
                room.room_clear()
                self.add_cash(room.fee)
                self.rooms_occupied.remove(room)

