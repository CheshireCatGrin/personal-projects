import Utilities

print("Welcome to Jordan's Rubix Cube Solver!")
print()
print("This program will allow you to enter in the arrangement of any 3 by 3 Rubix Cube and tell you the steps")
print("to solve it!")
print()
print('To begin, What colors are on your Rubix Cube? Enter these values as single letters (e.g. "R" for "red" without')
print('any extra spaces between entries (e.g. R,W,B,O,G,Y)')

reply = input(">>>")
while True:
    try:
        if Utilities.check_colors(reply) == 'no error':
            print()
            print("Are you satisfied with " + reply + ' as your colors?')
            if input(">>>") in ["yes", 'Yes', 'yeah', 'Yeah', 'Sure', 'sure']:
                break
            else:
                print("What are your six colors?")
                input(">>>")
                continue
        elif Utilities.check_colors(reply) in ['comma error', 'length error']:
            print("Formatting error. Please enter six colors separated by commmas.")
            reply = input(">>>")
            continue
        elif Utilities.check_colors(reply) in ['space error', 'value error']:
            print("Formatting error. Please enter your six colors as letters without any spaces. Thanks!")
            reply = input(">>>")
            continue
        elif Utilities.check_colors(reply) == 'duplicate error':
            print("Formatting error. Your cube cannot have the same color on two different sides.")
            reply = input(">>>")
            continue
    except:
        print("Formatting error. Please enter six colors separated by commmas.")
        reply = input(">>>")
        continue

colors_list = reply.split(',')
print()


print("Okay, pick any side of your Rubix Cube and I want you to tell me the arrangement of colors from the top-left ")
print("towards the right like you are reading a book. Here is an example of what it should look like:")

rubix_image = [" ___________ ", '| 1 | 2 | 3 |', '| 4 | 5 | 6 |', '| 7 | 8 | 9 |', ' ----------- ']

for e in rubix_image:
    print(" " * 10 + e)

print()
print('Your entry for this side of the cube should look like this: "1, 2, 3, 4, 5, 6, 7, 8, 9"')
print()

side_list = []

dialogue_list = [[],["This is important. DO NOT change the orientation of your Rubix cube. Simply look at the top",
                     " of your cube and then tell me once again the colors left to right"],
                     ["Okay, now rotate the cube back to the starting position, and then rotate it upside down ",
                      "to see the bottom. What are the tiles there?"],
                     ["Rotate back to the starting side. Now, rotate the cube to your right (to see the left side)."],
                     ["Rotate back to the startin side. Now, rotate the cube to your left (to see the right side)."],
                     ["Rotate back to the startin side. Finally, rotate your cube 180 degrees to get a look at the",
                     " back side."]]

for x in range(6):

    for e in dialogue_list[x]:
        print(e)
    reply = input(">>>")
    print()
    while True:
        if Utilities.check_side(reply, colors_list) == 'no error':
            side_list.append(reply)
            break
        elif Utilities.check_side(reply, colors_list) == 'comma error':
            print("Formatting error. Please enter the nine values separated by commmas.")
            reply = input(">>>")
            continue
        elif Utilities.check_side(reply, colors_list) == 'length error':
            print("Formatting error. Please enter nine and only nine values separated by commas.")
            reply = input(">>>")
            continue
        elif Utilities.check_side(reply, colors_list) == 'value error':
            print("Formatting error. One or more of the values you chose for the tiles does not appear in the colors on your")
            print("Rubix cube. Try again.")
            reply = input(">>>")
            continue

print()
print("Okay, now for the magic.")