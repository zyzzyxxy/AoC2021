
class Probe():
    def __init__(self, velocity_x, velocity_y, x_min, x_max, y_min, y_max ):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.location_x = 0
        self.location_y = 0
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.highest_y = 0

    def Step(self):
        self.location_x += self.velocity_x
        self.location_y += self.velocity_y
        self.updateVelocity()
        if self.location_y > self.highest_y:
            self.highest_y = self.location_y


    ##asume target below to right
    def Missed_target(self):
        missed = False
        if self.location_x > self.x_max:
            missed = True
        if self.location_y < self.y_min:
            missed = True
        return missed

    def in_target(self):
        if self.location_x <= self.x_max and self.location_x >= self.x_min and self.location_y >= self.y_min and self.location_y<= self.y_max :
           return True
        return False

    def updateVelocity(self):
        self.velocity_y -=1
        if self.velocity_x > 0:
            self.velocity_x -=1
        if self.velocity_x < 0:
            self.velocity_x +=1


def run():
    file = open("day17")
    X, Y = file.read().split("target area: ")[1].split(",")
    X = X.split("x=")
    Y = Y.split("y=")
    x_min, x_max = X[-1].split("..")
    y_min, y_max = Y[-1].split("..")
    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    print(x_min,x_max)
    print(y_min,y_max)

    highest_y = []
    hit_coordinates = []
    for x in range(100):
        for y in range(600):
            probe = Probe(x,y-300, x_min,x_max,y_min,y_max)
            while(not probe.Missed_target()):
                probe.Step()
                if(probe.in_target()):
                    print("probe hit target")
                    highest_y.append(probe.highest_y)
                    coord = (x,y-200)
                    if coord not in hit_coordinates:
                        hit_coordinates.append((x,y-200))

    print(hit_coordinates)
    print(len(hit_coordinates))
    print(highest_y.__len__())
    print((1,1)==(1,1))



if __name__ == "__main__":
    run()
