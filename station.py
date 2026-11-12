from bike import ElectroBike

class Stations:
    def __init__(self, name):
        self.name = name
        self.bikes = []


    def add_bike(self, bike):
        self.bikes.append(bike)

    def take_bike(self):
        for bike in self.bikes:
            if bike.can_be_issued():
                self.bikes.remove(bike)
                return bike
        return None



    def count(self):
         return len(self.bikes)



    def low_charge_bikes(self):
        result = []
        for bike in self.bikes:
            if isinstance(bike, ElectroBike) and bike.charge < 20:
                result.append((bike.numb, self.name, bike.charge))
        return result











