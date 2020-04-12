def welcome():
    p1 = "Player 1"
    p2 = "PLayer 2"
    print("Welcome to the tic tac toe game")
    while True:
        choice = input(f"{p1} : Do you want to be X or O? ")
        if choice != "X" or "O":
            print("Invalid input! Try again")
            continue
        player_1 = choice
        player_2 = "O" if player_1 == "X" else player_2 = "X"
    user_input(player_1, player_2)


def user_input(p1, p2):
    pointer = ["", "", "", "", "", "", "", "", ""]
    counter = 1
    while counter <= 10:
        i = str(input("Enter a number from 1 to 9"))
        if counter % 2 == 0:
            
        counter += 1
        if win_check(pointer, p1) is True:
            print("Winner is player 1")
            break
        if win_check(pointer, p2) is True:
            print("Winner is Player 2")
            break
    if counter == 9:
        print("It is a draw")
    again()


def board(indent):
    print(
        f" {indent[6]}  | {indent[7]}  | {indent[8]} \n"
        "------------\n"
        f" {indent[3]}  | {indent[4]}  | {indent[5]} \n"
        "------------\n"
        f" {indent[0]}  | {indent[1]}  | {indent[2]} \n"
    )


def win_check(lst, mark):
    if lst[0] == lst[1] == lst[2] == mark:
        return True
    elif lst[0] == lst[3] == lst[6] == mark:
        return True
    elif lst[0] == lst[4] == lst[8] == mark:
        return True
    elif lst[1] == lst[4] == lst[7] == mark:
        return True
    elif lst[2] == lst[5] == lst[8] == mark:
        return True
    elif lst[2] == lst[4] == lst[6] == mark:
        return True
    elif lst[3] == lst[4] == lst[5] == mark:
        return True
    elif lst[6] == lst[7] == lst[8] == mark:
        return True


def again():
    answer = input("Do you want to play again? ")
    if answer == "Yes":
        welcome()
    if answer == "No":
        print("See you later ma Friend")

welcome()

