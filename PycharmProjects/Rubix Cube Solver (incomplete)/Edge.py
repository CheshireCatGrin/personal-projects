from Edge import Edge
def transform(coord, trans):  # Applies a 3 by 3 linear transformation to any vector and outputs the vector
    return [(coord[0] * trans[0][0]) + (coord[1] * trans[1][0]) + (coord[2] * trans[2][0]),
            (coord[0] * trans[0][1]) + (coord[1] * trans[1][1]) + (coord[2] * trans[2][1]),
            (coord[0] * trans[0][2]) + (coord[1] * trans[1][2]) + (coord[2] * trans[2][2])]

class Edge(object):
    def __init__(self, rubix, color1, color2):
        self.rubix = rubix
        self.color1 = color1
        self.color2 = color2
        self.solve_color = color1
        self.cross_color = color2

        for pair in rubix.edges_map:
            edge_colors = [rubix.coords[pair[0]], rubix.coords[pair[1]]]
            if self.color1 in edge_colors and self.color2 in edge_colors:
                for color in edge_colors:
                    if edge_colors[0] == self.color1:
                        self.coord1 = edge_colors[0]
                        self.coord2 = edge_colors[1]
                    else:
                        self.coord1 = edge_colors[1]
                        self.coord2 = edge_colors[0]

        self.solve_coord = self.coord1
        self.cross_coord = self.coord2
        self.instructions = []

    def assign_colors(self, solve_color):
        if self.color1 == solve_color:
            self.solve_color = self.color1
            self.solve_coord = self.coord1

            self.cross_color = self.color2
            self.cross_coord = self.coord2
        else:
            self.solve_color = self.color2
            self.solve_coord = self.coord2

            self.cross_color = self.color1
            self.cross_coord = self.coord1

    def update_coord(self, trans):
        self.coord1 = transform(self.coord1, trans)
        self.coord2 = transform(self.coord2, trans)


