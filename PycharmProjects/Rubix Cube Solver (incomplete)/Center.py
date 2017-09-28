def transform(coord, trans):  # Applies a 3 by 3 linear transformation to any vector and outputs the vector
    return [(coord[0] * trans[0][0]) + (coord[1] * trans[1][0]) + (coord[2] * trans[2][0]),
            (coord[0] * trans[0][1]) + (coord[1] * trans[1][1]) + (coord[2] * trans[2][1]),
            (coord[0] * trans[0][2]) + (coord[1] * trans[1][2]) + (coord[2] * trans[2][2])]


class Center(object):
    def __init__(self, rubix, coord1, coord2, solve_color):
        self.rubix = rubix
        self.coord1 = coord1
        self.coord2 = coord2
        self.solve_color = solve_color

        for e in [rubix.coords[coord1], rubix.coords[coord2]]:
            if e != solve_color:
                self.non_solve_color = e

        for e in [self.coord1, self.coord2]:
            if rubix.coords[e] == solve_color:
                self.solve_coord = e
            else:
                self.non_solve_coord = e

    def get_coord(self, color):
        if color == self.solve_color:
            return
        if color == self.non_solve_color:
            return self.coord2

    def get_color(self, coord):
        if coord == self.coord1:
            return self.coord1color
        if coord == self.coord2:
            return self.coord2color

    def update_coords(self, trans):
        self.coord1 = transform(self.coord1, trans)
        self.coord2 = transform(self.coord2, trans)