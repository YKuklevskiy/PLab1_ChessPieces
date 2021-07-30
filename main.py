# Lab 1

# Написать 4 класса шахматных фигур. Каждая фигура должна иметь название,
# описание движения(как она ходит), а также функцию, в которую передается неопределенное
# количество точек с координатами (x, y), эта функция должна выдать число ходов,
# которые может совершить фигура из данной точки (доска - стандартная шахматная 8х8, на доске нет других фигур).
# Доп задания на плюсики.
# 1) Ввод и вывод точек для каждой фигуры из текстового файла
# Пример
# firstChP: 3-4; 2-3; 2-2
# secondChP: 2-2; 1-2
# thirdChP: 1-1
# fourthChP: 1-3; 3-3
# 2) Поле задается, т.е. оно не фиксировано (8 на 8), а может быть (4 на 5  или 7 на 3, 100 на 100).
# Значения поля от 1 до 100.


# Пример итогового ввода из файла:
# board: {width}-{length} задает размер доски (по умолчанию 8x8)
# {piece_name}: {x1}-{y1}; {x2}-{y2}; ... выводит возможные ходы на текущей доске в данных точках для данной фигуры

from Pieces import Pawn, King, Queen, Bishop, Knight, Rook


req = 'idle'
board_x = 8
board_y = 8
piece_names = {'pawn': Pawn(), 'king': King(), 'queen': Queen(),
               'bishop': Bishop(), 'knight': Knight(), 'rook': Rook()}


inp = open('input.txt', 'r')
out = open('output.txt', 'w')

for req in inp:
    req = req.lower().strip(' \n')
    if req == '':
        continue
    req_base = req.split(':')[0].strip(' ')
    if req_base == 'board':
        board_x = int(req.split(':')[1].split('-')[0].strip(' '))
        board_y = int(req.split(':')[1].split('-')[1].strip(' '))
        out.write(f'Board changed to {board_x}x{board_y}.\n')
    elif req_base in piece_names:
        points = req.split(':')[1].strip(' ').split(';')
        final_output = f'{piece_names[req_base].name}: '
        for point in points:
            if point.strip(' \n') == '':
                continue
            possible_moves = piece_names[req_base].possible_moves(board_x,
                                                                  board_y,
                                                                  int(point.split('-')[0].strip(' ')),
                                                                  int(point.split('-')[1].strip(' ')))
            final_output += f'{possible_moves}; '
        out.write(f'{final_output[:len(final_output) - 2]}.\n')
    else:
        out.write('Bad request\n')

inp.close()
out.close()
