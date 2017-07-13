import time
def end_game():
    end = "\
            ________________________________ \n\
           | X       Игра окончена!      O  |\n\
           |                                |\n\
           |    O (1)Вернуться в меню     X |\n\
           '--------------------------------'\n"
    mode = input(end)
    while mode!= '1':
        print('\n' * 30)
        print('       Неверный id действия. Попробуйте снова')
        mode = input(end)
    start_game()


def options():
    about = "\
            ________________________________ \n\
           | X      Игра разработана     O  |\n\
           |        Олегом Федотовым        |\n\
           |     <l.o.l.e.g.f@yandex.ru>    |\n\
           |                                |\n\
           |    O  (1)Вернуться в меню     X|\n\
           '--------------------------------'\n"
    mode = input(about)
    while mode!= '1':
        print('\n' * 30)
        print('       Неверный id действия. Попробуйте снова')
        mode = input(about)
    print('\n' * 30)
    start_game()



def add_symbol(small_table, table, symbol, k):
    i = (k - 1) % 3
    j = (k - 1) // 3
    if small_table[i][j] != '*':
        return False
    if symbol == 'X':
        table[5 * j + 1] = table[5 * j + 1][:8 * i + 2] + '\   /' + table[5 * j + 1][8 * i + 7:]
        table[5 * j + 2] = table[5 * j + 2][:8 * i + 2] + ' \ / ' + table[5 * j + 2][8 * i + 7:]
        table[5 * j + 3] = table[5 * j + 3][:8 * i + 2] + ' / \ ' + table[5 * j + 3][8 * i + 7:]
        table[5 * j + 4] = table[5 * j + 4][:8 * i + 2] + '/   \ ' + table[5 * j + 4][8 * i + 8:]
        small_table[i][j] = 'X'
    if symbol == 'O':
        table[5 * j + 1] = table[5 * j + 1][:8 * i + 2] + ' ___ ' + table[5 * j + 1][8 * i + 7:]
        table[5 * j + 2] = table[5 * j + 2][:8 * i + 2] + '|   |' + table[5 * j + 2][8 * i + 7:]
        table[5 * j + 3] = table[5 * j + 3][:8 * i + 2] + '|   |' + table[5 * j + 3][8 * i + 7:]
        table[5 * j + 4] = table[5 * j + 4][:8 * i + 2] + "'---'" + table[5 * j + 4][8 * i + 7:]
        small_table[i][j] = 'O'
    return True

def game_pvb():
    report = "\
            ________________________________ \n\
           | X                           O  |\n\
           |   К сожалению, данная функция  |\n\
           |  находится в стадии разработки |\n\
           |                                |\n\
           |      (1)Вернуться в меню       |\n\
           '--------------------------------'\n"
    mode = input(report)
    while mode!= '1':
        print('\n' * 30)
        print('       Неверный id действия. Попробуйте снова')
        mode = input(report)
    print('\n' * 30)
    start_game()


def game_pvp(player1, player2):
    small_table = [['*' for i in range(3)] for j in range(3)]
    table = [" _______________________ ",
             "|       |       |       |",
             "|       |       |       |",
             "|       |       |       |",
             "|       |       |       |",
             "|-------|-------|-------|",
             "|       |       |       |",
             "|       |       |       |",
             "|       |       |       |",
             "|       |       |       |",
             "|-------|-------|-------|",
             "|       |       |       |",
             "|       |       |       |",
             "|       |       |       |",
             "|       |       |       |",
             "'-------'-------'-------'"]

def printfield(table):
    for string in table:
        print(string)
def start_game():
    intro = "\
            ________________________________ \n\
           | X  Приветствуем Вас в игре  O  |\n\
           |      O     X            X      |\n\
           |  |/ |> Г Г- -т- | /| |/ | /|   |\n\
           |  |\ |  [ L_  |  |/ | |\ |/ |X  |\n\
           |       O    ------       X      |\n\
           | O |__| Г-i г-i | /| |/ | /|    |\n\
           |   |  | L_| j l |/ | |\ |/ |O   |\n\
           |    X               O           |\n\
           |  (1)Начать игру PlayerVSPlayer |\n\
           | O(2)Начать игру PlayerVSBot  O |\n\
           |  (3)Об Авторе  X        X      |\n\
           '--------------------------------'\n"
    mode = input(intro)
    print('\n' * 30)
    while mode not in ['1', '2', '3']:
        print('       Неверный id действия. Попробуйте снова')
        mode = input(intro)
        print('\n' * 30)
    if mode == '2':
        game_pvb()
    elif mode == '3':
        options()
    else:
        print('\n' * 30)
        player1 = input('      Введите никнейм первого игрока:\n')
        player2 = input('      Введите никнейм второго игрока:\n')
        game_pvp(player1, player2)



start_game()