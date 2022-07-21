
win_combinations = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {
    1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
is_game_on = True
turns_count = 0
player1_tiles = []
player2_tiles = []


def start_game():
    global is_game_on
    is_game_on = True
    board = ['-', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1 = '-'
    player2 = '-'
    ready_to_play = '-'
    print("**Welcome to Tic Tac Toe Game**")
    while(ready_to_play not in ['Y', 'N']):
        ready_to_play = input("Are you ready to play? Y or N ").upper()
    if(ready_to_play == 'N'):
        print("**GoodBye**")
        exit()
    while player1 not in ['X', 'O']:
        player1 = input("Hello Player 1! Do you want to be X or O? ").upper()
    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    print("Player 1 will go first")
    curr_player = player1
    display_board(board)
    player_move(board, player1, player2, curr_player)


def display_board(board):
    print('-------------')
    print('|', board[1], '|', board[2], '|', board[3], '|')
    print('-------------')
    print('|', board[4], '|', board[5], '|', board[6], '|')
    print('-------------')
    print('|', board[7], '|', board[8], '|', board[9], '|')
    print('-------------')


def player_move(board, player1, player2, curr_player):
    global player1_tiles
    global player2_tiles
    if not is_game_on:
        start_game()
    else:
        print(f"{curr_player} is now playing")
        choice = ''
        temp_choice = ''
        while choice not in range(1, 10) or board[choice] == 'X' or board[choice] == 'O':
            temp_choice = input("Choose an empty tile: ")
            if(temp_choice.isdigit() == True):
                choice = int(temp_choice)
        board[choice] = curr_player
        display_board(board)

        if(curr_player == player1):
            player1_tiles.append(choice)
            check_win(board, player1, player2, player1_tiles, curr_player)

        else:
            player2_tiles.append(choice)
            check_win(board, player1, player2, player2_tiles, curr_player)


def check_win(board, player1, player2, player_tiles, curr_player):
    global is_game_on
    global turns_count
    global player1_tiles
    global player2_tiles
    turns_count += 1
    for combination in win_combinations:
        if combination.issubset(player_tiles) or turns_count == 9:
            if combination.issubset(player_tiles):
                print(f"player {curr_player} is the winner")
            else:
                print("It's a draw!")
            player1_tiles = []
            player2_tiles = []
            turns_count = 0
            is_game_on = False

    if(curr_player == player1):
        curr_player = player2
    else:
        curr_player = player1

    player_move(board, player1, player2, curr_player)


start_game()