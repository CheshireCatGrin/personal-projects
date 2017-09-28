import Person
import PrintBox

def get_longest_name(gen):
    # input the list of names and it will return the an integer value representing the
    # length of the longest first-last name pair within the set of those names and their
    # ancestors

    name_tuples = []
    longest_name = 0

    for person in gen:
        name_tuples.append((person.first, person.last))

    for tuple in name_tuples:
        tuple_length = len(tuple[0]) + len(tuple[1])
        if tuple_length > longest_name:
            longest_name = tuple_length

    return longest_name

def get_gen_list(sibling_list):
    # Will generate a list of lists. The first list will contain the sibling-person objects. The second list will
    # contain the sibling's parent-objects. The third will contain the parents' parents objects and so on. Used to
    # print the family tree.
    gen_list = [sibling_list]
    gen_list.append([sibling_list[0].father, sibling_list[1].mother])

    while gen_list[-1][0].father != None:
        temp_list = []
        for e in gen_list[-1]:
            temp_list.append(e.father)
            temp_list.append(e.mother)
        gen_list.append(temp_list)
    return gen_list[::-1]

def concatenate_strings(l):
    cont_string = ""
    for e in l:
        cont_string = cont_string + e
    return cont_string

def printout(sibling_list):
    print(__name__)
    initial_spaces = 10
    gen_list = get_gen_list(sibling_list)

    i = 0
    halfway_marks = []

    for gen in gen_list:

        if get_longest_name(gen) > 10:
            total_length = get_longest_name(gen) + 6
            if total_length % 2 == 1:
                total_length += 1
        else:
            total_length = 16

        l0, l1, l2, l3, l4 = [[], [] ,[] ,[] ,[]]

        #if gen == gen_list[0]:
            #halfway_marks.append(int((total_length * 2 + initial_spaces) / 2))
        if len(gen) > 2:
            for n in range(1, int(len(gen)/2)):
                #halfway_marks.append(halfway_marks[i] + (total_length * 2 + initial_spaces * 2) * n)
                halfway_marks.append((total_length * 2 + initial_spaces * 2) * n)
        print("Halfway marks are: " + str(halfway_marks))

        for person in gen:
            #next_space = halfway_marks[i]
            next_space = halfway_marks[i] - int(total_length * 0.5) #- len(concatenate_strings(l0))
            #print(str(halfway_marks[i]) + " - " + str(int(total_length * 0.5)) + " - " + str(len(concatenate_strings(l0))) + " = " + str(next_space))
            '''
            print("Next space is: " + str(next_space))
            print("Halfwaymarks[i] is: " + str(halfway_marks[i]))
            '''
            #print("Total_length * 0.5 is: " + str(int(total_length * 0.5)))
            #print("len(concatenate_strings(l0): " + str(len(concatenate_strings(l0))))
            for line in [l0, l1, l2, l3, l4]:
                if gen == gen_list[0]:
                    if person != gen[0]:
                        line.append(" " * initial_spaces)
                else:
                    line.append(" " * next_space)
                    #print(next_space)

            l0.append(" " + "_" * int(total_length - 2) + " ")
            l1.append("| " + person.last + ", " + person.first + " " * (total_length - 5 - len(person.last) - len(person.first)) + "|")
            l2.append("|   Born: " + person.birth + " " * (total_length - 16) + " |")
            l3.append("|   Died: " + person.death + " " * (total_length - 16) + " |")
            l4.append("'" + "-" * (total_length - 2) + "'")

        i += 1
        print_list = list(map(concatenate_strings, [l0, l1, l2, l3, l4]))

        for e in print_list:
            t=0#print(e)

for row in range(0,len(info)):
    printBox.append(PrintBox.PrintBox(18))
    for column in range(0,len(info[row])):
        printBox[row].add_box(info[row][column])

for box in printBox:
    print(box.s1)
    print(box.s2)
    print(box.s3)
    print(box.s4)
    print(box.s5)