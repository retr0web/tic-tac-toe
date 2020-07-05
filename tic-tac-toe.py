cells = list("         ")  # playing field
player_char = "X"
game_over = False
turn = 0


def rules():
    print("This is playing field for tic-tac-toe")
    print("Each cell is represented as coordinate")
    print("6 | 7 | 8")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("0 | 1 | 2")
    print("Each turn you will be asked to enter coordinate")
    print("Each turn character changes from X to O automatically")
    print("Player X starts first")


def display_field():
    print("----------")
    print(cells[6] + " | " + cells[7] + " | " + cells[8])
    print("---------")
    print(cells[3] + " | " + cells[4] + " | " + cells[5])
    print("---------")
    print(cells[0] + " | " + cells[1] + " | " + cells[2])
    print("----------")


def enter_cell():
    global turn
    print("Enter cell coordinate")
    player_input = int(input())
    if 0 <= player_input < 9:
        if cells[player_input] == " ":
            cells[player_input] = player_char
            turn += 1
        else:
            print("Cell is occupied")
            enter_cell()
    else:
        print("You must enter number between 0-8")
        enter_cell()


def game_check():
    global game_over
    global turn
    if cells[0] == cells[1] == cells[2] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[3] == cells[4] == cells[5] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[6] == cells[7] == cells[8] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[0] == cells[3] == cells[6] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[1] == cells[4] == cells[7] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[2] == cells[5] == cells[8] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[0] == cells[4] == cells[8] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif cells[2] == cells[4] == cells[6] != " ":
        display_field()
        print("player " + player_char + " wins!")
        game_over = True
    elif turn == 9:
        display_field()
        print("Draw")
        game_over = True
    switch_char()


def switch_char():
    global player_char
    if player_char == "X":
        player_char = "O"
    else:
        player_char = "X"


def game():
    while not game_over:
        display_field()
        enter_cell()
        game_check()
        print("----------------------------")


rules()
game()
