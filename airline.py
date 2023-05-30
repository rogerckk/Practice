class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passangers = []
    
    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)

people = ["Ben", "Jack", "Ron", "Ken"]
for person in people:
    if flight.add_passanger(person):
        print(f"Added {person} to the flight successfully")
    else:
        print(f"No available seats for {person}")
