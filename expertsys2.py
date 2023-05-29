class Flight:
    def __init__(self, flight_number, source, destination, start_time, end_time):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.start_time = start_time
        self.end_time = end_time


class Cargo:
    def __init__(self, cargo_number, source, destination, start_time):
        self.cargo_number = cargo_number
        self.source = source
        self.destination = destination
        self.start_time = start_time


class ExpertSystem:
    def __init__(self):
        self.flights = []
        self.cargoes = []

    def add_flight(self, flight_number, source, destination, start_time, end_time):
        flight = Flight(flight_number, source, destination, start_time, end_time)
        self.flights.append(flight)

    def add_cargo(self, cargo_number, source, destination, start_time):
        cargo = Cargo(cargo_number, source, destination, start_time)
        self.cargoes.append(cargo)

    def get_flight_schedule(self, source, destination, start_time):
        available_flights = []

        for flight in self.flights:
            if flight.source == source and flight.destination == destination and flight.start_time >= start_time:
                available_flights.append(flight)

        return available_flights

    def get_cargo_schedule(self, source, destination, start_time):
        available_cargoes = []

        for cargo in self.cargoes:
            if cargo.source == source and cargo.destination == destination and cargo.start_time >= start_time:
                available_cargoes.append(cargo)

        return available_cargoes


# Create an instance of the ExpertSystem
expert_system = ExpertSystem()

# Add flights
expert_system.add_flight("F001", "London", "New_York", "09:00", "15:00")
expert_system.add_flight("F002", "Paris", "Tokyo", "12:00", "22:00")
expert_system.add_flight("F003", "New_York", "London", "10:30", "16:30")

# Add cargoes
expert_system.add_cargo("C001", "London", "New_York", "10:00")
expert_system.add_cargo("C002", "Paris", "Tokyo", "13:00")
expert_system.add_cargo("C003", "New_York", "London", "12:00")

# Get user input for flight search
flight_source = input("Enter the source airport: ")
flight_destination = input("Enter the destination airport: ")
flight_start_time = input("Enter the desired flight start time (format: HH:MM): ")

# Get flight schedule based on user input
flight_schedule = expert_system.get_flight_schedule(flight_source, flight_destination, flight_start_time)

# Display the flight schedule
if flight_schedule:
    print("Available flights:")
    for flight in flight_schedule:
        print(f"Flight Number: {flight.flight_number}, Source: {flight.source}, Destination: {flight.destination}, "
              f"Start Time: {flight.start_time}, End Time: {flight.end_time}")
else:
    print("No available flights matching the criteria.")

# Get user input for cargo search
cargo_source = input("Enter the source for Cargo: ")
cargo_destination = input("Enter the destination for Cargo: ")
cargo_start_time = input("Enter the desired cargo start time (format: HH:MM): ")

# Get cargo schedule based on user input
cargo_schedule = expert_system.get_cargo_schedule(cargo_source, cargo_destination, cargo_start_time)

if cargo_schedule:
    print("Available Cargo:")
    for cargo in cargo_schedule:
        print(f"Flight Number: {cargo.cargo_number}, Source: {cargo.source}, Destination: {cargo.destination}, "
              f"Start Time: {flight.start_time}")
else:
    print("No available Cargo matching the criteria.")

