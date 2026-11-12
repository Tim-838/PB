class RentalService:
    def __init__(self):
        self.total_revenue = 0
    def calculate_cost(self, bike, minutes):
        total = bike.cost_per_minute() * minutes
        return total
    def take_bike(self, customer, station):
        return station.take_bike()
    def return_bike(self, customer, bike, station, minutes):
        cost = self.calculate_cost(bike, minutes)
        paid = customer.charge(cost)
        station.add_bike(bike)
        if paid:
            self.total_revenue += cost
            return cost
        return None