import Utilities
from Utilities import transform

import Edge

class Rubix(object):
    def __init__(self):
        self.instructions = []
        self.coords = {}
        self.colors = ["W", "Y", "B", "G", "R", "O"]
        self.opp_colors = [["W", "Y"], ["B", "G"], ["R", "O"]]
        self.sides = {"F": (0, 0, 2), (0, 0, 2): "F", "B": (0, 0, -2), (0, 0, -2): "B",
                      "L": (-2, 0, 0), (-2, 0, 0): "L", "R": (2, 0, 0), (2, 0, 0): "R",
                      "U": (0, 2, 0), (0, 2, 0): "U", "D": (0, -2, 0), (0, -2, 0): "D"}
        self.coord_map =    {"F": [(-1, 1, 2), (0, 1, 2), (1, 1, 2),
                                   (-1, 0, 2), (0, 0, 2), (1, 0, 2),
                                   (-1, -1, 2), (0, -1, 2), (1, -1, 2)],
                             "B": [(1, 1, -2), (0, 1, -2), (-1, 1, -2),
                                   (1, 0, -2), (0, 0, -2), (-1, 0, -2),
                                   (1, -1, -2), (0, -1, -2), (-1, -1, -2)],
                             "U": [(-1, 2, -1), (0, 2, -1), (1, 2, -1),
                                   (-1, 2, 0), (0, 2, 0), (1, 2, 0),
                                   (-1, 2, 1), (0, 2, 1), (1, 2, 1)],
                             "D": [(-1, -2, 1), (0, -2, 1), (1, -2, 1),
                                   (-1, -2, 0), (0, -2, 0), (1, -2, 0),
                                   (-1, -2, -1), (0, -2, -1), (1, -2, -1)],
                             "R": [(2, 1, 1), (2, 1, 0), (2, 1, -1),
                                   (2, 0, 1), (2, 0, 0), (2, 0, -1),
                                   (2, -1, 1), (2, -1, 0), (2, -1, -1)],
                             "L": [(-2, 1, -1), (-2, 1, 0), (-2, 1, 1),
                                   (-2, 0, -1), (-2, 0, 0), (-2, 0, 1),
                                   (-2, -1, -1), (-2, -1, 0), (-2, -1, 1)]}

        self.edges_map = [[(0, 1, 2), (0, 2, 1)], [(-2, 1, 0), (-1, 2,  0)], [(2, 1, 0), (1, 2, 0)],
                      [(0, 2, -1), (0, 1, -2)], [(0, -1, 2), (0, -2, 1)], [(0, -2, -1), (0, -1, -2)],
                      [(-2, -1, 0), (-1, -2, 0)], [(2, -1, 0), (1, -2, 0)],
                      [(-1, 0, 2), (-2, 0, 1)], [(2, 0, 1), (1, 0, 2)], [(-2, 0, -1), (-1, 0, -2)],
                      [(2, 0, -1), (1, 0, -2)]]

        self.corners_map = [((-1, 2, 1), (-2, 1, 1), (-1, 1, 2)), ((1, 1, 2), (1, 2, 1), (2, 1, 1)),
                        ((-1, 1, -2), (-2, 1, -1), (-1, 1, -2)), ((2, 1, -1), (1, 2, -1), (1, 1, -2)),
                        ((-2, -1, 1), (-1, -1, 2), (-1, -2, 1)), ((2, -1, 1), (1, 2, 1), (1, -1, 2)),
                        ((-2, -1, -1), (-1, -2, -1), (-1, -1, -2)), ((2, -1, -1), (1, -2, -1), (1, -1, -2))]

        self.centers_map = [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]

        self.transformations = {"F": [[0, -1, 0], [1, 0, 0], [0, 0, 1]], "Fi": [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
                                "B": [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], "Bi": [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
                                "L": [[1, 0, 0], [0, 0, 1], [0, -1, 0]], "Li": [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
                                "R": [[1, 0, 0], [0, 0, -1], [0, 1, 0]], "Ri": [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
                                "U": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], "Ui": [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
                                "D": [[0, 0, -1], [0, 1, 0], [1, 0, 0]], "Di": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]}

        self.rotations = {(2, 0, 0): ("R", "Ri"), (-2, 0, 0): ("L", "Li"), (0, 2, 0): ("U", "Ui"), (0, -2, 0): ("D", "Di"), (0, 0, 2): ("F", "Fi"), (0, 0, -2): ("B", 'Bi')}

    def update_coords(self, list_of_sides):

        for e in list_of_sides:
            list_of_coords = self.coord_map[e[0]]
            for i in range(len(list_of_coords)):
               self.coords[list_of_coords[i]] = e[1][i]

        self.centers = {}
        for center in self.centers_map:
            self.centers[center] = self.coords[center]
            self.centers[self.coords[center]] = center

        #self.corners = {corner: self.coords[corner] for corner in self.corners_map}
        #self.edges = {edge: self.coords[edge] for edge in self.edges_map}


    def get_color(self, coord):
        return self.coords[coord]

    def get_opposite_color(self, color):
        for pair in self.opp_colors:
            if color in pair:
                for e in pair:
                    if e != color:
                        return e

    def get_center_coord(self, color):
        for e in self.centers_map:
            if self.coords[e] == color:
                return e

    def get_opposite_plane(self, color):
        # will return the color which is exactly opposite of the inputted color
        plane = list(self.centers[color])
        if 2 in plane:
            plane[plane.index(2)] = -2

        if -2 in plane:
            plane[plane.index(-2)] = 2

        return tuple(plane)

    def get_rotation(self, coord, spin):
        # Takes in the coord corrsponding to the center-side you wish to rotate and either
        # clockwise or counterclockwise and then outputs a rotation
        side = self.layercheck(coord)
        if spin == 'cw':
            return side
        if spin == 'ccw':
            return side + 'i'


    def check_cross_color_complete(self, edge):
        # This function will check to see if one color on the first layer cross is completed.
        return self.planecheck(edge.solve_coord, self.centers[edge.solve_color]) == "same" and self.planecheck(edge.cross_coord, self.centers[edge.cross_color]) == "same"

    def check_standard_pair(self, edge):
        # This function will check to see if the relevant edge has completed a standard pair i.e. the cross_color
        # is matched with its color side and therefore we need only to rotate on the cross-color axis until we have
        # completed that portion of the first layer cross.
        return self.planecheck(edge.cross_coord, self.centers[edge.cross_color]) == "same"

    def check_inverted_pair(self, edge):
        # This function will check to see if the relevant edge has completed an inverted pair, which is the same as the
        # standard pair except that the edge needs to be flipped.
        return self.planecheck(edge.solve_coord, self.centers[edge.cross_color]) == "same"

    def check_direction(self, coord1, coord2, color):
        # This will return a "direction" for an edge piece. The possible outputs are "away", 'toward',
        # 'adjacent'
        if self.planecheck(coord1, self.centers[color]) == 'same' or self.planecheck(coord2, self.centers[color]) == 'same':
            return 'toward'
        elif self.planecheck(coord1, self.centers[color]) == 'opposite' or self.planecheck(coord2, self.centers[color]) == 'opposite':
            return 'away'
        else:
            return 'adjacent'

    def wincheck(self):
        sides = ["F", 'B', "U", "D", "L", "D"]

        list_of_values = []
        for side in sides:
            list_of_values.append([self.coords[tuple(vector)] for vector in self.coord_map[side]])

        for l in list_of_values:
            value = l[0]
            for e in l:
                if e != value:
                    return False
                else:
                    continue
        return True

    def planecheck(self, coord1, coord2):
        # will return 'same', 'opposite', or 'adjacent' iff two coords, respectively, exist on the same plane, the
        # opposite planes, or adjacent planes

        for e in zip(coord1, coord2):
            if e[0] in [-2, 2] and e[1] in [-2, 2] and e[0] == e[1]:
                return 'same'
        for e in zip(coord1, coord2):
            if e[0] in [-2, 2] and e[1] in [-2, 2] and e[0] != e[1]:
                return 'opposite'
        return 'adjacent'

    def layercheck(self, coord): # Input a coordinate and it will output the corresponding plane on which the coordinate is found.
        if coord[0] == 2:
            return "R"
        if coord[0] == -2:
            return "L"
        if coord[1] == 2:
            return "U"
        if coord[1] == -2:
            return "D"
        if coord[2] == 2:
            return "F"
        if coord[2] == -2:
            return "B"

    def quicker_rotation(self, vector_to_move, target_center, axis_of_rotation):
        # Will return the quicker of two rotations that move the vector_to_move onto the same plane as the target vector

        two_rotations = self.rotations[axis_of_rotation]
        orig_vector = vector_to_move
        counter1, counter2 = [0, 0]
        for index in range(2):
            while self.planecheck(vector_to_move, target_center) != 'same':
                vector_to_move = transform(vector_to_move, self.transformations[two_rotations[index]])
                if index == 0:
                    counter1 += 1
                if index == 1:
                    counter2 += 1
            vector_to_move = orig_vector
        if counter1 <= counter2:
            return [two_rotations[0] for x in range(counter1)]
        else:
            return [two_rotations[1] for x in range(counter1)]


    def rotate(self, rotation, basis = None, get = None):

        '''
        The dictionary, 'd', below has two elements to check whether a vector meets the criteria for being affected by
        the relevant Rubix cube rotation. This method will do one of two things depending on whether the *get*
        argument is anything other than the default 'no.' If no argument is passed, the method will update the
        self.coords with the rotated vectors. If any argument is passed, the method will return
        the resultant coordinates would be without updating the self.coords.
        '''

        d = {"F": (2, (2, 1)), "Fi": (2, (2,1)), "B": (2, (-1, -2)), "Bi": (2, (-1, -2)),
             "L": (0, (-1, -2)), "Li": (0 ,(-1, -2)), "R": (0 ,(1, 2)), "Ri": (0, (1, 2)),
             "U": (1, (1, 2)), "Ui": (1, (1, 2)), "D": (1, (-1, -2)), "Di": (1, (-1, -2))}

        entries = d[rotation]

        vectors, converted_vectors, values = [[], [], []]
        for i in self.coords:
            i = list(i)
            if i[entries[0]] == entries[1][0] or i[entries[0]] == entries[1][1]:
                vectors.append(i)
                converted_vectors.append(transform(i, self.transformations[rotation]))
                values.append(self.coords[tuple(i)])
                toconvert = zip(converted_vectors, values)

        if get == None:
            for e in toconvert:
                self.coords[tuple(e[0])] = e[1]
        else:
            new_coords = self.coords.copy()
            for e in toconvert:
                new_coords[tuple(e[0])] = e[1]
            return new_coords

    def printface (self):
        '''
        This method will print out an image representing the current rubix cube faces.
        '''

        l0= ["Front Side", "Back Side", "Top Side", "Bottom Side", "Left Side", "Right Side"]

        l1 = [(str(self.coords[(0, 2, 0)]) + " facing up"),
                       (str(self.coords[(0, 2, 0)]) + " facing up"),
                       (str(self.coords[(0, 0, -2)]) + " facing up"),
                       (str(self.coords[(0, 0, 2)]) + " facing up"),
                       (str(self.coords[(0, 2, 0)]) + " facing up"),
                       (str(self.coords[(0, 2, 0)]) + " facing up")]

        l2 = [(str(self.coords[-1, 1, 2]) + " " + str(self.coords[0, 1, 2]) + " " + str(self.coords[1, 1, 2])),
              (str(self.coords[1, 1, -2]) + " " + str(self.coords[0, 1, -2]) + " " + str(self.coords[-1, 1, -2])),
              (str(self.coords[-1, 2, -1]) + " " + str(self.coords[0, 2, -1]) + " " + str(self.coords[1, 2, -1])),
              (str(self.coords[-1, -2, 1]) + " " + str(self.coords[0, -2, 1]) + " " + str(self.coords[1, -2, 1])),
              (str(self.coords[-2, 1, -1]) + " " + str(self.coords[-2, 1, 0]) + " " + str(self.coords[-2, 1, 1])),
              (str(self.coords[2, 1, 1]) + " " + str(self.coords[2, 1, 0]) + " " + str(self.coords[2, 1, -1]))]

        l3 = [(str(self.coords[-1, 0, 2]) + " " + str(self.coords[0, 0, 2]) + " " + str(self.coords[1, 0, 2])),
              (str(self.coords[1, 0, -2]) + " " + str(self.coords[0, 0, -2]) + " " + str(self.coords[-1, 0, -2])),
              (str(self.coords[-1, 2, 0]) + " " + str(self.coords[0, 2, 0]) + " " + str(self.coords[1, 2, 0])),
              (str(self.coords[-1, -2, 0]) + " " + str(self.coords[0, -2, 0]) + " " + str(self.coords[1, -2, 0])),
              (str(self.coords[-2, 0, -1]) + " " + str(self.coords[-2, 0, 0]) + " " + str(self.coords[-2, 0, 1])),
              (str(self.coords[2, 0, 1]) + " " + str(self.coords[2, 0, 0]) + " " + str(self.coords[2, 0, -1]))]

        l4 = [(str(self.coords[-1, -1, 2]) + " " + str(self.coords[0, -1, 2]) + " " + str(self.coords[1, -1, 2])),
              (str(self.coords[1, -1, -2]) + " " + str(self.coords[0, -1, -2]) + " " + str(self.coords[-1, -1, -2])),
              (str(self.coords[-1, 2, 1]) + " " + str(self.coords[0, 2, 1]) + " " + str(self.coords[1, 2, 1])),
              (str(self.coords[-1, -2, -1]) + " " + str(self.coords[0, -2, -1]) + " " + str(self.coords[1, -2, -1])),
              (str(self.coords[-2, -1, -1]) + " " + str(self.coords[-2, -1, 0]) + " " + str(self.coords[-2, -1, 1])),
              (str(self.coords[2, -1, 1]) + " " + str(self.coords[2, -1, 0]) + " " + str(self.coords[2, -1, -1]))]

        s = 20
        strings = []
        for e in [l0, l1, l2, l3, l4]:
            string = ""
            for x in e:
                string += x + (" " * (s - len(x)))
            strings.append(string)

        for e in strings:
            print(e)