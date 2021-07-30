from Piece import Piece


class Pawn(Piece):
    name = 'Pawn'
    description = 'The weakest piece of them all. Can move only 1 square forward (two if in starting position), ' \
                  'and can only eat pieces on the next forward diagonal squares.'

    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        if pos_y < 1 or pos_x < 1 or size_y < pos_y or size_x < pos_x:
            return 'Piece\'s outside the board'
        if size_y == pos_y:
            return '0'
        if pos_y == 2 and size_y != 2:
            return str(min(size_y-pos_y, 2))
        else:
            return '1'


class King(Piece):
    name = 'King'
    description = 'The most valuable piece. If it can\'t defend or move and is under attack, you lose. ' \
                  'It can move one square in all directions.'

    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        if pos_y < 1 or pos_x < 1 or size_y < pos_y or size_x < pos_x:
            return 'Piece\'s outside the board'
        wall_touches = 0
        consecutive_touch = False
        if pos_y == 1:
            wall_touches += 1
        if pos_x == 1:
            wall_touches += 1
        if pos_y == size_y:
            wall_touches += 1
        if pos_x == size_x:
            wall_touches += 1
        if pos_x == size_x == 1 or pos_y == size_y == 1:
            consecutive_touch = True
        if wall_touches == 0:
            return '8'
        elif wall_touches == 1:
            return '5'
        elif wall_touches == 2:
            if consecutive_touch:
                return '2'
            else:
                return '3'
        elif wall_touches == 3:
            return '1'
        else:
            return '0'


class Queen(Piece):
    name = 'Queen'
    description = 'The most powerful piece. It is very valuable so it must be used with care. ' \
                  'Can move diagonally, horizontally and vertically across the board.'

    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        if pos_y < 1 or pos_x < 1 or size_y < pos_y or size_x < pos_x:
            return 'Piece\'s outside the board'
        total_moves = 0
        total_moves += min(size_y - pos_y, pos_x - 1)
        total_moves += min(size_y - pos_y, size_x - pos_x)
        total_moves += min(pos_y - 1, pos_x - 1)
        total_moves += min(pos_y - 1, size_x - pos_x)
        total_moves += size_y + size_x - 2
        return str(total_moves)


class Knight(Piece):
    name = 'Knight'
    description = 'Piece with the strangest movement. ' \
                  'Can move only in L shapes (3 squares forward, 1 to the side), but in all directions.'

    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        if pos_y < 1 or pos_x < 1 or size_y < pos_y or size_x < pos_x:
            return 'Piece\'s outside the board'
        total_moves = 0
        if pos_x-1 >= 3:
            if pos_y-1 > 0:
                total_moves += 1
            if size_y-pos_y > 0:
                total_moves += 1
        if size_x-pos_x >= 3:
            if pos_y-1 > 0:
                total_moves += 1
            if size_y-pos_y > 0:
                total_moves += 1
        if pos_y-1 >= 3:
            if pos_x-1 > 0:
                total_moves += 1
            if size_x-pos_x > 0:
                total_moves += 1
        if size_y-pos_y >= 3:
            if pos_x-1 > 0:
                total_moves += 1
            if size_x-pos_x > 0:
                total_moves += 1
        return str(total_moves)


class Bishop(Piece):
    name = 'Bishop'
    description = 'Piece of the same value of Knight (or a tiny bit more, if you wish). ' \
                  'Can move only diagonally across the board.'

    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        if pos_y < 1 or pos_x < 1 or size_y < pos_y or size_x < pos_x:
            return 'Piece\'s outside the board'
        total_moves = 0
        total_moves += min(size_y-pos_y, pos_x-1)
        total_moves += min(size_y-pos_y, size_x-pos_x)
        total_moves += min(pos_y-1, pos_x-1)
        total_moves += min(pos_y-1, size_x-pos_x)
        return str(total_moves)


class Rook(Piece):
    name = 'Rook'
    description = 'A powerful piece that can move horizontally and vertically across the board.'

    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        if pos_y < 1 or pos_x < 1 or size_y < pos_y or size_x < pos_x:
            return 'Piece\'s outside the board'
        return str(size_y + size_x - 2)
