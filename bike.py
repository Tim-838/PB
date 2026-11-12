class Bike:
    def __init__(self, numb):
        self.numb = numb
    def cost_per_minute(self):
        return 2
    def can_be_issued(self):
        return True
class ElectroBike(Bike):
    def __init__(self, numb):
        super().__init__(numb)
    def cost_per_minute(self):
        return 5
    def can_be_issued(self):
        return True
