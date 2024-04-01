class Airline:
    def __init__(self, flight_number: str, origin: str, destination: str, departure_time: str, duration: list[int]):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration

    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes {self.duration[2]} seconds"

    def get_flight_info(self):
        return f"Flight {self.flight_number} from {self.origin} to {self.destination} departs at {self.departure_time} and lasts {self.get_duration()}"
