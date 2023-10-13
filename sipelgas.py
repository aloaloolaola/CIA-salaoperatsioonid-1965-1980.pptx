Xr, Yr, Zr = [int(a) for a in input().split(" ")]
Xs, Ys, Zs = [int(a) for a in input().split(" ")]
Xm, Ym, Zm = [int(a) for a in input().split(" ")]

class Cuboid:
    def __init__(self, Xr, Yr, Zr, Xs, Ys, Zs, Xm, Ym, Zm):
        self.Xr = Xr
        self.Yr = Yr
        self.Zr = Zr
        self.Xs = Xs
        self.Ys = Ys
        self.Zs = Zs
        self.Xm = Xm
        self.Ym = Ym
        self.Zm = Zm



    def normalise_rotation(self):
        if Xs == 0: self.rotate(0, 3, 0)
        elif Xs == Xr: self.rotate(0, 1, 0)
        elif Ys == 0: self.rotate(1, 0, 0)
        elif Ys == Yr: self.rotate(3, 0, 0)
        elif Zs == Zr: self.rotate(2, 0, 0)

        if Xm == 0: self.rotate(0, 0, 1)
        elif Ym == Yr: self.rotate(0, 0, 2)
        elif Xm == Xr: self.rotate(0, 0, 3)

        return self

    def rotate(self, Rx, Ry, Rz):
        if Rx > 0:
            for i in range(Rx):
                self.Yr, self.Zr = self.Zr, self.Yr
                
                self.Ys, self.Zs = self.Yr - self.Zs, self.Ys
                self.Ym, self.Zm = self.Yr - self.Zm, self.Ym
        elif Ry > 0:
            for i in range(Ry):
                self.Xr, self.Zr = self.Zr, self.Xr
                
                self.Xs, self.Zs = self.Zs, self.Zr - self.Xs
                self.Xm, self.Zm = self.Zm, self.Zr - self.Xm
        else:
            for i in range(Rz):
                self.Xr, self.Yr = self.Yr, self.Xr
                
                self.Xs, self.Ys = self.Xr - self.Ys, self.Xs
                self.Xm, self.Ym = self.Xr - self.Ym, self.Xm

    def unwrap_position(self, X, Y, Z):
        #print(X, Y, Z)
        if Z == 0:
            return [(X, Y)]
        elif Y == 0:
            return [(-Z, -X), (X, -Z), (self.Xr + Z, X - self.Xr)]
        elif Z == self.Zr:
            return [(-self.Yr + Y, self.Yr + self.Zr + X), (X, 2 * self.Yr + self.Zr - Y), (self.Xr + self.Yr - Y, self.Yr + self.Zr + self.Xr - X),
                    (self.Xr + self.Zr + Y, -self.Xr + X), (2 * self.Xr + self.Zr - X, Y), (self.Xr + self.Zr + self.Yr - Y, self.Yr + self.Xr - X),
                    (self.Xr + Y, -self.Zr - self.Xr + X), (X, -self.Zr - Y), (-Y, -self.Zr - X),
                    (-self.Zr - self.Yr + Y, self.Yr + X), (-self.Zr - X, Y), (-self.Zr - Y, -X)]
        #print("Asi on imelikus kohas??!!", Z, self.Zr)

    def measure_distance(self):
        ant_pos = self.unwrap_position(self.Xs, self.Ys, self.Zs)[0]
        honey_positions = self.unwrap_position(self.Xm, self.Ym, self.Zm)
        distance = 0
        for honey_pos in honey_positions:
            if distance == 0:
                distance = ((ant_pos[0]-honey_pos[0]) ** 2 + (ant_pos[1] - honey_pos[1]) ** 2) ** (1/2)
            else:
                distance = min(((ant_pos[0]-honey_pos[0]) ** 2 + (ant_pos[1] - honey_pos[1]) ** 2) ** (1/2), distance)
        return distance


cuboid = Cuboid(Xr, Yr, Zr, Xs, Ys, Zs, Xm, Ym, Zm).normalise_rotation()
#print(cuboid)
print(cuboid.measure_distance())