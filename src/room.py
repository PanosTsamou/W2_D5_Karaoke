class Room:
    
    def __init__(self, input_room_capacity, input_fee, input_songs):
        self.guests = []
        self.songs = input_songs
        self.room_capacity = input_room_capacity
        self.fee = input_fee
