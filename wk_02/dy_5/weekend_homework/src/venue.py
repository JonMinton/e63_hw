class Venue:
    def __init__(self, name, fee, rooms, till):
        self.name = name
        self.fee = fee
        self.rooms = rooms
        self.till = till
        self.guests = []

    def admit_guest(self, guest):
        if guest.wallet >= self.fee:
            guest.wallet -= self.fee
            self.till += self.fee
            self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def transfer_guest_to_room(self, guest, room):
        if len(room.guests) < room.capacity:
            room.checkin_guest(guest)
            self.guests.remove(guest)

    def transfer_guest_from_room(self, guest, room):
        room.checkout_guest(guest)
        self.guests.append(guest)
