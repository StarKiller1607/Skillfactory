import time as t
print('Добро пожаловать в игру крестики-нолики!')
t.sleep(1)
player1 = input('Имя первого игрока (X): ')
player2 = input('Имя второго игрока (O): ')

available_moves = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
move_count = 1

def step(f: list[list], move: str) -> str:
    global move_count
    f[int(move[0])][int(move[1])] = 'x' if move_count % 2 != 0 else 'o'
    for ii in f:
        print(*ii)
    return f[int(move[0])][int(move[1])]

def win_check(l_move: str) -> (bool, str):
    global field
    player = player1 if l_move == 'x' else player2
    for k in range(1, 4):
        if all(n == l_move for n in field[k][1:]):
            return True, player

    diagonals = [[], []]
    for l in range(1, 4):
        diagonals[0].append(field[l][l])
        diagonals[1].append(field[l][4 - l])
        column = []
        for m in range(1, 4):
            column.append(field[m][l])
        if all(r == l_move for r in column):
            return True, player

    for diagonal in diagonals:
        if all(x == l_move for x in diagonal):
            return True, player

    return False, player

field = [
        [' ', '1', '2', '3'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-'],
        ['3', '-', '-', '-']
    ]

print('\nИнструкция:\n')
skip = input('Пропустить инструкцию? (Y/N): ')
if skip not in 'Yy':

    field_instruction = [
        [' ', '1', '2', '3'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-'],
        ['3', '-', '-', '-']
    ]
    #Перепробовал все способы копирования списка, и через .copy() и через срез, и через append([:])
    #По какой-то причине в любом случае изменение field_instruction изменяет и исходный field

    print('\n--------------------------------------------------------------------------------\nЭто игровое поле:\n')

    for j in field_instruction:
        print(*j)
        t.sleep(0.5)
    t.sleep(1)

    print('\nДля указания своего хода используйте координатный метод с использованием цифр по краям поля'); t.sleep(4)
    print('\nПишите цифры без пробела, как двузначное число (11)'); t.sleep(3)
    print('\nПервая цифра - это строка, вторая - столбец'); t.sleep(3)
    print('\nКаждому игроку по очереди будет предлагаться ввести свой ход'); t.sleep(3)
    print('\nНапример:'); t.sleep(2)

    print('\nХод игрока "Игрок №1": 11')
    field_instruction[1][1] = 'x'
    for j in field_instruction:
        print(*j)
    t.sleep(4)

    print('\nХод игрока "Игрок №2": 12')
    field_instruction[1][2] = 'o'
    for j in field_instruction:
        print(*j)
    t.sleep(4)

    input('\nЧтобы начать игру, нажмите Enter')

print('--------------------------------------------------------------------------------\nНачало игры!\n'); t.sleep(1)

for i in field:
    print(*i)
    t.sleep(0.5)
t.sleep(0.5)

while True:
    if move_count % 2 != 0:
        player1_move = input(f'\nХод игрока {player1}: ')
        while player1_move not in available_moves:
            player1_move = input(f'Неверно указан ход, попробуйте ещё раз (доступные ходы - {available_moves}): ')
        last_move = step(field, player1_move)
        available_moves.remove(player1_move)
    else:
        player2_move = input(f'\nХод игрока {player2}: ')
        while player2_move not in available_moves:
            player2_move = input(f'Неверно указан ход, попробуйте ещё раз (доступные ходы - {available_moves}): ')
        last_move = step(field, player2_move)
        available_moves.remove(player2_move)

    if move_count > 4:
        winner = win_check(last_move)
        if winner[0]:
            print(f'\n----------------------\nПобедил игрок {winner[1]}!\n----------------------')
            break

    move_count += 1
    if move_count > 9:
        print('\n-------\nНичья!\n-------')
        break
