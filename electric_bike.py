class ElectricBike:
    def __init__(self, number, charge):
        self.number = number
        self.charge = charge
        self.price_per_minute = 5

    def can_be_rented(self):
        return self.charge >= 20

    def get_battery_info(self):
        return {"number": self.number,"charge": self.charge}


def get_low_battery_bikes(stations):
    low_battery = []
    for station in stations:
        for bike in station.bikes:
            if hasattr(bike, "charge") and bike.charge < 20:
                low_battery.append({"number": bike.number, "station": station.name, "charge": bike.charge})
    return low_battery