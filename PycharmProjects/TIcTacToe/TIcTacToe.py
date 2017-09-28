'''
The Structure of my Program:
    - The data representing the values of the rows and columns of tic-tac toe are stored in the variable "board."
    The variable board is a dictionary, with keys 11,12,13,21,22,23,31,32,33. The tens place represents the row
    and the ones place represents the columns. The idea of this program is to update this dictionary as the players
    enter their moves.
    - The function print_board will print out the current variable 'board' into an easily readable format
    - After introducing the program to the players and storing their names in variables, the program will ask for input.
    - The input will immediately run through the error_check function, which in order
        (a) uses the check_comma function to make sure there is a comma, and then split(',') to break up the user input
        into a list without the commas.
        (b) use len() to check whether the list has exactly two elements
        (c) use the try function to attempt to convert both elements to integers
        (d) use check_values to see if the the entries are between 1 and 3
        (e) use check_occupied_spot to see if the entry is not already filled in
    If any of these components of error_check produce an error, it will output True. Else, False.
    - The program will then call the function update_board which will combine the numbers entered by the player to
    create a key, which will then mutate 'board' appropriately.
    - The current_player variable is a list storing two elements: (1) an integer, either 1 or 2, representing that
    player and (2) the name of that player.
    - After updating the board, the function update_player will change the values in current_player
    to the next player
    - The program will then run through two more checks: (1) win_check and (2) stalemate_check.
    - win_check is composed of three functions, row_check, col_check, and diagonal_check. Each one will check whether
    a win condition has been met in those three ways
    - stalemate_check will check whether 'board' has any hyphens (empty space) left. If so, it will output True
    - if win_check and stalemate_check output False, the program will then update_player and iterate until either
    the win_check and stalemate_check output True.
    - when either win_check or stalemate_check output True, new dialogue will be triggered printing the outcome and
    asking players if they would like to continue. If input is affirmative, 'board' will be reset and loop will
    continue. Else, program will end.
'''


def print_board(lst):  # will take as an input "board" and print out an image representing the board
    print("     C1  C2  C3")
    print("R1:  " + str(lst[11]) + "   " + str(lst[12]) + "   " + str(lst[13]))
    print("R2:  " + str(lst[21]) + "   " + str(lst[22]) + "   " + str(lst[23]))
    print("R3:  " + str(lst[31]) + "   " + str(lst[32]) + "   " + str(lst[33]))


def check_comma(n):  # will check the user-input to ensure they have entered a comma
    return n.find(',') != -1


def check_values(row, col):  # will check the row and column of user input to ensure both values are between 1 and 3
    return row <= 3 and row >= 1 and col <= 3 and col >= 1


def check_occupied_spot(row, col, lst):  # will check whether an attempted user-input is already filled in
    index = 10 * row + col
    return lst[index] == '-'


def update_board(n, player, lst):  # will update the variable "board" with "X" or "O"
    n = n.split(',')
    row = int(n[0])
    col = int(n[1])
    key = 10 * row + col
    if player == 1:
        lst[key] = 'X'
    else:
        lst[key] = 'O'


def error_check(n):  # Returns True if any of the error conditions are true, and prints the reason why

    if check_comma(n):
        n = n.split(',')
    else:
        print("I'm sorry. You need to enter a comma between the row and column entries. Try again.")
        print()
        return True

    if len(n) != 2:
        print(
            "I'm sorry. You must enter 2 and only 2 values for the row and column representing your entry. Try again.")
        print()
        return True

    try:
        row = int(n[0])
        col = int(n[1])
    except:
        print("I'm sorry. You need to enter integer values representing the row and column of your entry. Try again.")
        print()
        return True

    if not check_values(row, col):
        print("I'm sorry. Your entries can be no greater than 3. There are only three rows and columns! Try again.")
        print()
        return True
    elif not check_occupied_spot(row, col, board):
        print("I'm sorry. That spot has already been taken. Please choose a different location.")
        return True
    else:
        return False


def row_check(l, player):  # will return True iff player has three in a row.
    keys = [11, 12, 13]
    i = 0
    while i < 3:
        row = [l[x] for x in keys]
        if row.count(player) == 3:
            return True
        else:
            keys = [x + 10 for x in keys]
            i += 1
            continue
    return False


def col_check(l, player):  # will return True iff player has three in a column.
    keys = [11, 21, 31]
    i = 0
    while i < 3:
        col = [l[x] for x in keys]
        if col.count(player) == 3:
            return True
        else:
            keys = [x + 1 for x in keys]
            i += 1
            continue
    return False


def diagonal_check(l, player):  # will return True iff player has three in a diagonal.
    keys = [11, 22, 33]
    for x in range(2):
        diag = [l[x] for x in keys]
        if diag.count(player) == 3:
            return True
        else:
            keys = [31, 22, 13]
            continue
    return False


def win_check(l, player):  # will return True if row_check, col_check, or diagonal_check return True
    if player == 1:
        player = 'X'
    else:
        player = 'O'
    return row_check(l, player) or col_check(l, player) or diagonal_check(l, player)


def stalemate_check(l):  # will output True iff game has reached a stalemate
    if '-' in l.values():
        return False
    else:
        return True


def update_player(player):  # will update the two elements of current_player list to next player
    if player[0] == 1:
        player[0] = 2
        player[1] = player2
        return player
    else:
        player[0] = 1
        player[1] = player1
        return player


def check_reply_yesno(reply):  # will check whether a reply is acceptable (i.e. yes or no)
    return reply == 'yes' or reply == 'Yes' or reply == 'no' or reply == 'No'


board = {11: '-', 12: '-', 13: '-', 21: '-', 22: '-', 23: '-', 31: '-', 32: '-', 33: '-'}
reply_list = ['no', 'No', 'nope', 'nope', 'nah', 'negative']
print("works")
while True:
    print("-" * 100)
    print("Welcome to Jordan's Tic-Tac-Toe Game!")
    print()
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    print()
    print("It's " + player1 + ' versus ' + player2 + '!')
    print()
    print("Are you ready to crush your opponent?")
    print()
    reply = input(">>> ")
    print()
    if reply in reply_list:
        print("Well, what are you waiting for?")
        continue
    else:
        break

print_board(board)
prompt = player1 + ", where will you strike first?"
current_player = [1, player1]

while True:

    print(prompt)
    print()

    while True:
        entry = input("Enter <Row>,<Column>:")
        if error_check(entry):
            continue
        else:
            break

    update_board(entry, current_player[0], board)
    print_board(board)
    print()

    if stalemate_check(board):
        print('What a fight! You have reached a stalemate. Would you like to play again?')
        print('<yes> or <no>')
        print()

        while True:
            reply = input('>>> ')
            if check_reply_yesno(reply):
                break
            else:
                print("I'm sorry. I only understand " + '"yes" or "no." Try again?')

        if reply == 'yes' or 'Yes':
            board = {11: '-', 12: '-', 13: '-', 21: '-', 22: '-', 23: '-', 31: '-', 32: '-', 33: '-'}
            continue
        else:
            print("Thanks for playing!")
            break

    elif win_check(board, current_player[0]):
        print(current_player[1] + ' wins!')
        print()
        print("Would you like to play again?")
        print("<yes> or <no>")
        print()

        while True:
            reply = input('>>> ')
            if check_reply_yesno(reply):
                break
            else:
                print("I'm sorry. I only understand " + '"yes" or "no." Try again?')

        if reply == 'yes' or reply == 'Yes':
            board = {11: '-', 12: '-', 13: '-', 21: '-', 22: '-', 23: '-', 31: '-', 32: '-', 33: '-'}
            continue
        else:
            print("Thanks for playing!")
            break
    else:
        current_player = update_player(current_player)
        prompt = "Your move, " + current_player[1] + '.' ""