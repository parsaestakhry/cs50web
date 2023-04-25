class Flight():
    def __init__(self , capacity) -> None:
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False 
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["parsa " , "melika" , "saba" , "ali"]

for person in people:
    if flight.add_passenger(person):
        print(f"{person} is added to flight.")
    else:
        print(f"{person} didn't make it to the flight.")