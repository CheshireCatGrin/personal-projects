from Edge import Edge
import itertools

transformations = {"F": [[0, -1, 0], [1, 0, 0], [0, 0, 1]], "Fi": [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
                                "B": [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], "Bi": [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
                                "L": [[1, 0, 0], [0, 0, 1], [0, -1, 0]], "Li": [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
                                "R": [[1, 0, 0], [0, 0, -1], [0, 1, 0]], "Ri": [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
                                "U": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], "Ui": [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
                                "D": [[0, 0, -1], [0, 1, 0], [1, 0, 0]], "Di": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]}

def transform(coord, trans):  # Applies a 3 by 3 linear transformation to any vector and outputs the vector
    return [(coord[0] * trans[0][0]) + (coord[1] * trans[1][0]) + (coord[2] * trans[2][0]),
            (coord[0] * trans[0][1]) + (coord[1] * trans[1][1]) + (coord[2] * trans[2][1]),
            (coord[0] * trans[0][2]) + (coord[1] * trans[1][2]) + (coord[2] * trans[2][2])]

def generate_opp_coords(center_coord):
    l = [[0, 2], [0, -2], [2, 0], [-2, 0]]
    opp_coords = []

    if 2 in center_coord:
        two_index = center_coord.index(2)
    else:
        two_index = center_coord.index(-2)

    for pair in l:
        new_coord = pair[:two_index] + [two_index] + pair[two_index:]
        opp_coords.append(tuple(new_coord))
        new_coord = pair[:two_index] + [-two_index] + pair[two_index:]
        opp_coords.append(tuple(new_coord))

    return opp_coords


def solvecross(rubix):
    completed_pairs = []
    iterations = []
    rubixes = []
    rubixes.append(rubix)

    for r in rubixes:
        for color in r.colors:
            cross_colors = [e for e in r.colors if e != color and e != r.get_opposite_color(color)]
            cross_color_perms = itertools.permutations(cross_colors)
            color_instructions = [[color, e] for e in cross_color_perms]
            iterations += color_instructions

        for instruction in iterations:
            solving_color = instruction[0]
            cross_color_order = instruction[1]
            for cross_color in cross_color_order:

                edge = Edge(r, solving_color, cross_color)

                solving_center_coord = r.get_center_coord(edge.solve_color)
                cross_center_coord = r.get_center_coord(edge.cross_color)

                while not r.check_cross_color_complete(edge):

                    if r.check_standard_pair(edge):

                        rotation_to_perform, num_rotations = r.quicker_rotation(edge.solve_coord, solving_center_coord, cross_center_coord)
                        new_r = r.copy()
                        instructions = [rotation_to_perform for num_rotations in range(num_rotations)]
                        for i in instructions:
                            new_r.instructions.append(i)
                            new_r.rotate(i)
                            rubixes.append(new_r)

                    elif r.check_inverted_pair(edge):
                        if r.check_direction(edge.solve_coord, edge.cross_coord, edge.solve_color) == 'away':
                            # The 'instructions' variable below stores the four lists of instructions corresponding to
                            # the four ways to solve this portion of the cube. The result will be four unique rubixes
                            # to iterate over.


                            '''
                            instructions = [[[edge.solve_coord, 'ccw'], [new_r.centers[solving_color], 'ccw'],
                                             [edge.cross_coord, 'cw'], [new_r.centers[solving_color], 'cw']],
                                            [[edge.solve_coord, 'cw'], [new_r.centers[solving_color], 'cw'],
                                             [edge.cross_coord, 'ccw'], [new_r.centers[solving_color], 'ccw']],
                                            [[edge.cross_coord, 'cw'], [edge.solve_coord, 'cw'], [edge.cross_coord, 'ccw']],
                                            [[edge.cross_coord, 'ccw'], [edge.solve_coord, 'ccw'], [edge.cross_coord, 'cw']]]'''

                            for method in instructions:
                                new_rubix = r.copy()
                                new_edge = edge.copy()
                                for i in method:
                                    new_rubix.instructions.append(new_rubix.get_rotation(i[0], i[1]))
                                    new_rubix.rotate(new_rubix.get_rotation(i[0], i[1]))
                                    new_edge = Edge(new_rubix, solving_color, cross_color)
                                rubixes.append(new_rubix)


def check_colors(string):
    if string.find(',') == -1:
        return 'comma error'
    l = string.split(",")
    for e in l:
        if e.find(" ") != -1:
            return 'space error'

    if not len(set(l)) == len(l):
        return "duplicate error"
    if len(l) != 6:
        return 'length error'
    for e in l:
        if len(e) != 1:
            return 'value error'
    return 'no error'

def check_side(side, colors_list):
    if side.find(',') == -1:
        return 'comma error'
    l = side.split(",")
    if len(l) != 9:
        return "length error"
    for e in l:
        if not e in colors_list:
            return "value error"
    return 'no error'

def check_solvable(side_list, colors_list):
    list_of_centers = [x[4] for x in side_list]
    list_of_center_outsides = [[x[1], x[3], x[5], x[7]] for x in side_list]
    list_of_corners = [[x[0], x[2], x[6], x[8]] for x in side_list]

    print(list_of_centers)
    print(list_of_center_outsides)
    print(list_of_corners)

    if len(set(list_of_centers)) != len(list_of_centers):
        return False

    for l in [list_of_center_outsides, list_of_corners]:
        c1, c2, c3, c4, c5, c6 = [0, 0, 0, 0, 0, 0]
        counter_list = [c1, c2, c3, c4, c5, c6]
        i = 0
        while i < 6:
            for e in l:
                counter_list[i] += e.count(colors_list[i])
            i += 1
        for e in counter_list:
            if e != 4:
                return False