# зададим поле.
# Поле у нас будет одномерным списком (list) с числами от 1 до 9.
# Для создания воспользуемся функцией range()

board = list(range(1, 10))


# напишем функцию, которая будет рисовать игровое поле.
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


# Формируем возможность ввода пользователем  данных в игру.
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try: # конструкция для неправильных значений вводе try-except-print
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


# задаем кортедж выйгрышных значений и цикл проверки текущих значений
# Если символы во всех трех заданных клетках равны - возвращаем выигрышный символ,
# иначе - возвращаем значение False.
# непустая строка (наш выигрышный символ) при приведении ее к логическому типу вернет True

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


# Главная функция, в которой происходит игра
# счетчик чередует возможность ввода Х и О
# всего не более 9 ходов
def main(board, takeInput=None):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            takeInput("X")
        else:
            takeInput("O")
        counter += 1
        if counter > 4:  # выигрыш не возможен до 5 хода
            tmp = check_win(board)  # чтобы не вызывать функцию check_win
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)
