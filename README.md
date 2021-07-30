# PLab1_ChessPieces
First Lab from Uni - Chess Pieces Classes

Reads input from input.txt in form of:
  {request}: {arg1}; {arg2}; ...


Commands:

board - change board size, takes one pair of arguments - measurements of board

piece_name - print amount of available moves for a piece in taken coordinates, takes multiple pairs of parameters - coordinates of initial places,
             writes the answer for each point on the board
             
Writes output to output.txt

Piece.py - contains base class for any Chess Piece class

Pieces.py - contains all available Chess Piece classes

Available classes: Pawn, King, Queen, Bishop, Knight, Rook
