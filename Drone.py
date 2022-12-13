class Drone():
    speed:float

    def __init__(self,speed:float):
        self.speed=float(speed)

    def getMaxSpeed(self)->float:
        maxSpeed=((self.speed)*(2/3))
        return maxSpeed

    def getMaxTemp(self)->float:
        return (104)

    def getLowTemp(self)->float:
        return (32)

    def getMaxHumidity(self)->float:
        return (85)