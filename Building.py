class Building:

    def __init__(self, minFloor, maxFloor, elevators):
        self.maxFloor = maxFloor
        self.elevators = elevators
        self.minFloor = minFloor

    def getElev(self, elev):
        return self.elevators[elev]