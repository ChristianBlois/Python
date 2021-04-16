import random, time

def print_guide_board():
    print("7|8|9")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("1|2|3")

def new_board():
    board = {"upperLeft": " ", "upperMiddle": " ", "upperRight": " ",
             "midLeft": " ", "midMiddle": " ", "midRight": " ",
             "bottomLeft": " ", "bottomMiddle": " ", "bottomRight": " "}
    return board

def set_letters():
    while True:
        print("What letter do you want to be? X or O?", end=" ")
        letter = input().upper()
        if letter == "X":
            player_letter = "X"
            computer_letter = "O"
            break
        elif letter == "O":
            player_letter = "O"
            computer_letter = "X"
            break
        else:
            print("Please enter X or O.")
    return [player_letter, computer_letter]

def first_move():
    players = ["Player", "Computer"]
    turn = random.choice(players)
    return turn

def print_board(current_board):
    print(current_board["upperLeft"] + "|" + current_board["upperMiddle"] + "|" + current_board["upperRight"])
    print("-+-+-")
    print(current_board["midLeft"] + "|" + current_board["midMiddle"] + "|" + current_board["midRight"])
    print("-+-+-")
    print(current_board["bottomLeft"] + "|" + current_board["bottomMiddle"] + "|" + current_board["bottomRight"])

def get_player_move(current_board):
    while True:
        decision = int(input())
        if decision >= 1 and decision <= 9:
            if decision == 1:
                decision = "bottomLeft"
            elif decision == 2:
                decision = "bottomMiddle"
            elif decision == 3:
                decision = "bottomRight"
            elif decision == 4:
                decision = "midLeft"
            elif decision == 5:
                decision = "midMiddle"
            elif decision == 6:
                decision = "midRight"
            elif decision == 7:
                decision = "upperLeft"
            elif decision == 8:
                decision = "upperMiddle"
            elif decision == 9:
                decision = "upperRight"
            if current_board[decision] == " ":
                break
            else:
                print("Enter an empty space.")
    return decision

def make_move(current_board, letter, move):
    current_board[move] = letter

def is_winner(current_board, letter):
    # Top horizontal
    if current_board["upperLeft"] == letter and current_board["upperMiddle"] == letter and current_board["upperRight"] == letter:
        return True
    # Mid horizontal
    elif current_board["midLeft"] == letter and current_board["midMiddle"] == letter and current_board["midRight"] == letter:
        return True
    # Bottom horizontal
    elif current_board["bottomLeft"] == letter and current_board["bottomMiddle"] == letter and current_board["bottomRight"] == letter:
        return True
    # Left vertical
    elif current_board["upperLeft"] == letter and current_board["midLeft"] == letter and current_board["bottomLeft"] == letter:
        return True
    # Mid vertical
    elif current_board["upperMiddle"] == letter and current_board["midMiddle"] == letter and current_board["bottomMiddle"] == letter:
        return True
    # Right vertical
    elif current_board["upperRight"] == letter and current_board["midRight"] == letter and current_board["bottomRight"] == letter:
        return True
    # Cross 1
    elif current_board["upperLeft"] == letter and current_board["midMiddle"] == letter and current_board["bottomRight"] == letter:
        return True
    # Cross 2
    elif current_board["upperRight"] == letter and current_board["midMiddle"] == letter and current_board["bottomLeft"] == letter:
        return True
    else:
        return False

def board_is_full(current_board):
    empty_spaces = 0
    for value in current_board.values():
        if value == " ":
            empty_spaces += 1
    if empty_spaces == 0:
        return True
    else:
        return False

def check_game(board, turn, letter):
    if is_winner(board, letter):
        print()
        print(f"{turn} wins!!")
        print()
        print_board(board)
        print()
        game_is_playing = False
        return [turn, False]
    else:
        if board_is_full(board):
            print()
            print("IT'S A TIE")
            print()
            print_board(board)
            print()
            game_is_playing = False
            return [turn, False]
        else:
            if turn == "Computer":
                turn = "Player"
                return ["Player", True]
            else:
                turn = "Computer"
                return ["Computer", True]

def get_computer_move(current_board, letter):
    if letter == "X":
        player_let = "O"
    elif letter == "O":
        player_let = "X"
    # First try to make a winning move.
    copy_board = current_board.copy()
    for key in copy_board.keys():
        if current_board[key] == " ":
            make_move(copy_board, letter, key)
            if is_winner(copy_board, letter):
                return key
    # Second, try to avoid loosing the game.
    copy_board = current_board.copy()
    for key in copy_board.keys():
        if current_board[key] == " ":
            make_move(copy_board, player_let, key)
            if is_winner(copy_board, player_let):
                return key
    # Third, try to make one of the corners.
    corner_moves = ["upperLeft", "upperRight", "bottomLeft", "bottomRight"]
    possible_corner_moves = []
    for corner in corner_moves:
        if copy_board[corner] == " ":
            possible_corner_moves.append(corner)
    if len(possible_corner_moves) > 0:
        choice = random.choice(possible_corner_moves)
        return choice
    # Fourth, try to make the center.
    if copy_board["midMiddle"] == " ":
        choice = "midMiddle"
        return choice
    # Fifth, try to make one of the sides.
    side_moves = ["upperMiddle", "midRight", "midLeft", "bottomMiddle"]
    possible_side_moves = []
    for side in side_moves:
        if copy_board[side] == " ":
            possible_side_moves.append(side)
    if len(possible_side_moves) > 0:
        choice = random.choice(possible_side_moves)
        return choice    

def game(board, turn, player_letter, computer_letter):
    game_is_playing = True
    move_number = 1
    print()
    print_board(board)
    while game_is_playing:
        time.sleep(1)
        print()
        # Player
        if turn == "Player":
            print(f"Move {move_number}: {turn}.", end=" ")
            player_move = get_player_move(board)
            make_move(board, player_letter, player_move)
            print_board(board)
            turn, game_is_playing = check_game(board, turn, player_letter)
            move_number += 1
        # Computer
        else:
            print(f"Move {move_number}: {turn}.")
            computer_move = get_computer_move(board, computer_letter)
            make_move(board, computer_letter, computer_move)
            print_board(board)
            turn, game_is_playing = check_game(board, turn, computer_letter)
            move_number += 1

def play_again():
    print("Do you want to play again? Y or N.", end=" ")
    while True:
        again = input().upper()
        if again == "Y" or again == "N":
            break
        else:
            print("Type Y or N.")
            continue
    if again == "Y":
        tic_tac_toe()
    else:
        print()
        print("Goodbye!")
        return False

def tic_tac_toe():
    while True:
        print()
        time.sleep(0.5)
        print_guide_board()
        print()
        board = new_board()
        player_letter, computer_letter = set_letters()
        turn = first_move()
        game(board, turn, player_letter, computer_letter)
        if not play_again():
            break

# Program
print("TIC TAC TOE!")
tic_tac_toe()