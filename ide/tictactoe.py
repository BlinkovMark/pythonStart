# Blinkov Mark TA21V Tic-tac-toe game
# For better gaming experience use numpad ;)
cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Owin = 0
Xwin = 0


# this function outputs the playing board
def printer():
    print(f' {cells[6]} | {cells[7]} | {cells[8]}\n'
          f' _ | _ | _\n'
          f' {cells[3]} | {cells[4]} | {cells[5]}\n'
          f' _ | _ | _\n'
          f' {cells[0]} | {cells[1]} | {cells[2]}')


# this function checks if the cell is already occupied by another player
def is_not_occupied(index):
    if cells[index] != 'X' or 'O':
        return True


# this function checks all possible ways to win and returns True if someone won
def check_the_winners():
    rsl = False
    if cells[0] == cells[1] == cells[2]:
        print(f'WINNER {cells[0]}')
        rsl = True
    if cells[3] == cells[4] == cells[5]:
        print(f'WINNER {cells[3]}')
        rsl = True
    if cells[6] == cells[7] == cells[8]:
        print(f'WINNER {cells[6]}')
        rsl = True
    if cells[0] == cells[3] == cells[6]:
        print(f'WINNER {cells[0]}')
        rsl = True
    if cells[1] == cells[4] == cells[7]:
        print(f'WINNER {cells[1]}')
        rsl = True
    if cells[2] == cells[5] == cells[8]:
        print(f'WINNER {cells[2]}')
        rsl = True
    if cells[0] == cells[4] == cells[8]:
        print(f'WINNER {cells[0]}')
        rsl = True
    if cells[2] == cells[4] == cells[6]:
        print(f'WINNER {cells[2]}')
        rsl = True
    return rsl


# main game logic
def game():
    global cells
    cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gaming = True
    turn = 1
    moves = 0
    while gaming:
        if turn == 1:
            printer()
            if check_the_winners():
                global Owin
                Owin += 1
                break
            try:
                print('Player 1 turn')
                choice = int(input('Choose а cell: '))
                if choice in cells and is_not_occupied(choice - 1):
                    cells[choice - 1] = '\033[0;34mX\033[0;0m'
                    moves += 1
                    turn = 2
            except ValueError:
                print('Invalid input')
        if turn == 2:
            printer()
            if check_the_winners():
                global Xwin
                Xwin += 1
                break
            if moves == 9:
                print('DRAW!')
                break
            try:
                print('Player 2 turn')
                choice = int(input('Choose а cell: '))
                if choice in cells and is_not_occupied(choice - 1):
                    cells[choice - 1] = '\033[2;33mO\033[0;0m'
                    moves += 1
                    turn = 1
            except ValueError:
                print('Invalid input')


# game stats
def stats():
    print(f'X won {Xwin} times')
    print(f'O won {Owin} times\n')


# main menu
def menu():
    print('Tic-tac-toe')
    using = True
    while using:
        print(f'1. Start game\n'
              f'2. Stats\n'
              f'3. Exit')
        i = int(input('Choose аn option: '))
        if i == 1:
            game()
        if i == 2:
            stats()
        if i == 3:
            print('Bye!')
            using = False


# run the program
if __name__ == '__main__':
    menu()