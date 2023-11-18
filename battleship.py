import time as t
import random as r
import copy

class Board:
    def __init__(self):
        self.board = [
            ['O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O'],
        ]

        self.board_copy = copy.deepcopy(self.board)
        self.blank_board = copy.deepcopy(self.board)
        self.win_check = 0

    def place_ship(self, decks: int, x: int, y: int, rotation: bool) -> bool:
        for k in range(len(self.board)):
            self.board_copy[k] = self.board[k].copy()
        for i in range(decks):
            try:
                if self.board_copy[y][x] == '■' or self.board_copy[y][x] == '*':  #russian O
                    return False
                else:
                    self.board_copy[y][x] = '■'
                    try:
                        if not rotation:
                            if i == 0 and x != 0:
                                self.board_copy[y][x-1] = '*'    #russian O
                                if y != 0:
                                    self.board_copy[y-1][x-1] = '*'  #russian O
                            if y != 0:
                                self.board_copy[y - 1][x] = '*'  # russian O
                            if i+1 == decks:
                                self.board_copy[y][x+1] = '*'  # russian O
                                if y != 0:
                                    self.board_copy[y-1][x+1] = '*'  # russian O
                        else:
                            if i == 0 and y != 0:
                                self.board_copy[y-1][x] = '*'    #russian O
                                if x != 0:
                                    self.board_copy[y-1][x-1] = '*'  #russian O
                            if x != 0:
                                self.board_copy[y][x-1] = '*'  # russian O
                            if i+1 == decks:
                                self.board_copy[y+1][x] = '*'  # russian O
                                if x != 0:
                                    self.board_copy[y+1][x-1] = '*'  # russian O
                        #self.board[y-1][x] = '8' #russian O
                    except IndexError:
                        pass

                    try:
                        if not rotation:
                            if i == 0 and x != 0:
                                self.board_copy[y + 1][x - 1] = '*'  # russian O
                            self.board_copy[y + 1][x] = '*'  # russian O
                            if i + 1 == decks:
                                self.board_copy[y + 1][x + 1] = '*'  # russian O
                        else:
                            if i == 0 and y != 0:
                                self.board_copy[y - 1][x + 1] = '*'  # russian O
                            self.board_copy[y][x+1] = '*'  # russian O
                            if i + 1 == decks:
                                self.board_copy[y + 1][x + 1] = '*'  # russian O
                        #self.board[y + 1][x] = '8'  # russian O
                    except IndexError:
                        pass

            except IndexError:
                return False

            if not rotation:
                x += 1
            else:
                y += 1

        for j in range(len(self.board_copy)):
            self.board[j] = self.board_copy[j].copy()
        return True

    def print_board(self):
        print('\nДоска игрока:')
        print('\t0 1 2 3 4 5')
        print('\t_ _ _ _ _ _')
        for i in range(len(self.board)):
            print(f'{i} |', *self.board[i])

    def shot(self, x: int, y: int) -> bool:
        try:
            if self.board[y][x] == '■':
                self.board[y][x] = 'X'
                self.win_check += 1
            elif self.board[y][x] == 'X' or self.board[y][x] == 'T':
                return False
            else:
                self.board[y][x] = 'T'
        except IndexError:
            return False

        return True

    def win(self):
        if self.win_check == 11:
            return True
        else:
            return False

    def clear_board(self):
        self.board = copy.deepcopy(self.blank_board)
        self.board_copy = copy.deepcopy(self.blank_board)


class AIBoard(Board):
    def print_board(self):
        print('\nДоска ИИ:')
        print('\t0 1 2 3 4 5')
        print('\t_ _ _ _ _ _')
        for i in range(len(self.blank_board)):
            print(f'{i} |', *self.blank_board[i])

    def shot(self, x: int, y: int) -> bool:
        try:
            if self.board[y][x] == '■':
                self.blank_board[y][x] = 'X'
                self.board[y][x] = 'X'
                self.win_check += 1
            elif self.board[y][x] == 'X' or self.board[y][x] == 'T':
                return False
            else:
                self.blank_board[y][x] = 'T'
                self.board[y][x] = 'T'
        except IndexError:
            return False

        return True


class Ship:

    def __init__(self, decks):
        self.decks = decks
        print(f'\nУстановка {self.decks}-палубного корабля:')
        self.x = int(input('Координата по горизонтали > '))
        while self.x not in range(0, 6):
            self.x = int(input('Координаты должны быть в диапазоне от 0 до 5, попробуйте ещё раз > '))
        self.y = int(input('Координата по вертикали > '))
        while self.y not in range(0, 6):
            self.y = int(input('Координаты должны быть в диапазоне от 0 до 5, попробуйте ещё раз > '))
        self.rotation = True if input('Повернуть корабль по вертикали? (Y/N) > ') in 'Yy' else False

    def get_decks(self):
        return self.decks

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_rotation(self):
        return self.rotation

class AIShip(Ship):
    def __init__(self, decks: int, x: int, y: int, rotation: bool):
        self.decks = decks
        self.x = x
        self.y = y
        self.rotation = rotation


class Player:
    def __init__(self):
        self.board = Board()



class Game:

    @staticmethod
    def generate_board():
        print('ИИ расставляет корабли . . .\n')
        a = 0
        while True:
            layout = []
            for i in range(7):
                if i == 0:
                    layout.append(AIShip(3, r.randint(0, 5), r.randint(0, 5), r.choice([True, False])))
                elif 0 < i < 3:
                    layout.append(AIShip(2, r.randint(0, 5), r.randint(0, 5), r.choice([True, False])))
                else:
                    layout.append(AIShip(1, r.randint(0, 5), r.randint(0, 5), False))

            for j in range(7):
                if not ai_board.place_ship(layout[j].get_decks(), layout[j].get_x(), layout[j].get_y(), layout[j].get_rotation()):
                    ai_board.clear_board()
                    break
                if j == 6:
                    a += 1

            if a:
                break

    @staticmethod
    def round():
        print('-'*50)
        print('> ХОД ИГРОКА <')
        ai_board.print_board()
        print('Ведите координаты, по которым хотите произвести выстрел:')
        while not ai_board.shot(int(input('Координата по горизонтали > ')), int(input('Координата по вертикали > '))):
            print('По указанным координатам уже был произведён выстрел, либо указаны координаты за пределами поля\n')
            print('Попробуйте ещё раз:\n')
        ai_board.print_board()

        print('\n> ХОД ИИ <')
        print('ИИ сделал выстрел по вашей доске:')
        while not player_board.shot(r.randint(0, 5), r.randint(0, 5)):
            pass
        player_board.print_board()


    @staticmethod
    def greet():
        print('Добро пожаловать в игру Морской Бой!');t.sleep(1)
        print('Игра проходит между ИИ и игроком')




ai_board = AIBoard()
Game().generate_board()


player_board = Board()
print('Игрок расставляет корабли . . .')
for i in range(7):
    if i == 0:
        new_ship = Ship(decks=3)
    elif 0 < i < 3:
        new_ship = Ship(decks=2)
    else:
        new_ship = Ship(decks=1)
    while not player_board.place_ship(new_ship.get_decks(), new_ship.get_x(), new_ship.get_y(), new_ship.get_rotation()):
        print('\nНеверное расположение корабля, попробуйте ещё раз:')
        if i == 0:
            new_ship = Ship(decks=3)
        elif 0 < i < 3:
            new_ship = Ship(decks=2)
        else:
            new_ship = Ship(decks=1)
    player_board.print_board()

while True:
    Game.round()
    if player_board.win():
        print('ПОБЕДИЛ ИИ!')
        break
    if ai_board.win():
        print('ПОБЕДИЛ ИГРОК!')
        break




























'''while not player_board.win():
    player_board.shot(int(input('x > ')), int(input('y > ')))
    player_board.print_board()
if player_board.win():
    print('win')'''



















'''player_board = Board()
ai_board = Board() # ai_board должен быть объектом класса AIBoard(), а щас он объект Board() для наглядности в консоли!!!


if not player_board.place_ship(3, 2, 2, False):
    print('b')

if not player_board.place_ship(3, 5, 0, False):
    print('a')

if not ai_board.place_ship(3, 1, 1, True):
    print('c')

player_board.shot(3, 2)
ai_board.shot(2, 1)

player_board.print_board()
ai_board.print_board()'''



