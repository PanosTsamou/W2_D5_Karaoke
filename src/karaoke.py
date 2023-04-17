class Karaoke:
    
    def __init__(self, input_rooms, input_cash, input_bar):
        self.all_rooms = input_rooms
        self.cash = input_cash
        self.bar = input_bar
        self.rooms_occupied = []
        self.waiting_list = []

    def add_cash(self, amount):
        self.cash += amount

    def find_room_is_free(self, room):
        if room in self.rooms_occupied:
            return False
        else:
            return True

    
    def check_in(self, add_room , add_booking):
        if add_room.fee <= add_booking.guest.wallet and add_booking.guest.age >= 18 and add_room.room_avaible  and add_room.check_if_they_fit(add_booking.number_people):
            add_room.add_guests(add_booking.guest)
            add_room.hours_occupied = add_booking.guest.hours_to_stay
            self.rooms_occupied.append(add_room)

                
    def check_in_with_search(self,add_room, add_booking):
        if add_room.fee <= add_booking.guest.wallet and add_booking.guest.age >= 18 and add_room.room_avaible  and add_room.check_if_they_fit(add_booking.number_people):
            add_room.add_guests(add_booking.guest)
            add_room.hours_occupied = add_booking.guest.hours_to_stay
            self.rooms_occupied.append(add_room)
            self.bar.add_items_in_tab_and_increase_money(add_booking.guest)
        elif  self.fitted_room(add_booking) is not None:
            self.fitted_room(add_booking).add_guests(add_booking.guest)
            self.fitted_room(add_booking).hours_occupied = add_booking.guest.hours_to_stay
            self.rooms_occupied.append(self.fitted_room(add_booking))
            self.bar.add_items_in_tab_and_increase_money(add_booking.guest)
        elif self.fitted_room(add_booking) is  None:
                for room in self.rooms_occupied:
                    if room.room_capacity == add_booking.number_people and room.fee <= add_booking.guest.wallet and room.room_avaible and add_booking.guest.age >= 18:
                        self.waiting_list.append(add_booking)
                        self.bar.add_guest_in_the_bar(add_booking.guest)
                        self.bar.add_items_in_tab_and_increase_money(add_booking.guest)
                

    def fitted_room(self, booking):
        results = None
        for room in self.all_rooms:
            if room.room_capacity == booking.number_people and room.fee <= booking.guest.wallet and room.room_avaible and booking.guest.age >= 18:
                results = room
        if results is None:
            for room in self.all_rooms:
                if room.room_capacity < booking.number_people and room.fee <= booking.guest.wallet and room.room_avaible and booking.guest.age >= 18:
                    results = room
        return results    

    def cheer_loudly(self, guest_booking):
        for room in self.rooms_occupied:
            if guest_booking.guest in room.guests and room.free_songs.find_song_in_list(guest_booking.guest.pref_song):
                return "whooooo" 
        return "sorry"

        

    def check_out(self, booking):
        for room in self.rooms_occupied:
            if booking.guest in room.guests:
                booking.guest.decrease_monies(room.fee)
                room.room_clear()
                self.add_cash(room.fee )
                self.rooms_occupied.remove(room)

    def check_out_with_tab(self, booking):
        for room in self.rooms_occupied:
            if booking.guest in room.guests:
                result = room.fee + self.bar.pay_for_bar_tab(booking.guest)
                booking.guest.decrease_monies(result)
                self.add_cash(room.fee)
                self.bar.add_monies( self.bar.pay_for_bar_tab(booking.guest))
                room.room_clear()
                self.rooms_occupied.remove(room)
