from imgs import *
import pygame

class Piece:
    img = None
    global BLACK_PIECE, WHITE_PIECE
    rect = (7, 7, 637, 637)

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    def validMoves(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win):
        if self.color == "white":
            drawThis = WHITE_PIECE[self.img]
        else:
            drawThis = BLACK_PIECE[self.img]       
        
        x = self.col * round(self.rect[2]/8)
        y = self.row * round(self.rect[2]/8)
        # print(x, y,)
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 76, 76), 2)

        win.blit(drawThis, (x, y))

class King(Piece):
    img = 0
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []
        return moves
        
class Queen(Piece):
    img = 1
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []
        return moves

class Bishop(Piece):
    img = 2
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []
        return moves

class Knight(Piece):
    img = 3
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []
        return moves

class Rook(Piece):
    img = 4
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []
        return moves

class Pawn(Piece):
    img = 5
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False

    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j =  self.row, self.col
        print(i, j)
        moves = []
# BLACK PAWNS
        if self.color == 'black':
            f1 = board.board[i+1][j]
            # FIRST MOVE WITH TWO OPTIONS
            if self.first:
                f2 = board.board[i+2][j]
                if not f1:
                    moves.append(('safe single jump', i+1, j))
                    if not f2:
                        moves.append(('safe double jump', i+2, j))
            # NORMAL SINGLE STEP MOVE
            else:
                if not f1:
                    moves.append(('safe single jump', i+1, j))
            # print(f1, f2)

            # KILLING DIAGONAL PIECES
            if j < 7 and i < 7:
                rd = board.board[i+1][j+1]
                if rd is not None:
                   moves.append(("Kill right down", i+1, j+1))
                   print(rd, "on right down")
            if j > 0 and i < 7:
                ld = board.board[i+1][j-1]
                if ld is not None:
                   moves.append(("Kill left down", i+1, j-1))
                   print(ld, 'on left down')
# WHITE PAWNS
        elif self.color == 'white':
            f1 = board.board[i-1][j]
            # FIRST MOVE WITH TWO OPTIONS
            if self.first:
                f2 = board.board[i-2][j]
                print(f1, f2)
                if not f1:
                    moves.append(('safe single jump', i-1, j))
                    if not f2:
                        moves.append(('safe double jump', i-2, j))
            # NORMAL SINGLE STEP MOVE
            else:
                if not f1:
                    moves.append(('safe single jump', i-1, j))
            # print(f1, f2)

            # KILLING DIAGONAL PIECES
            if j < 7 and 0 < i:
                ru = board.board[i-1][j+1]
                if ru is not None:
                   moves.append(("Kill right up", i-1, j+1))
                   print(ru, "on right up")
            if j > 0 and 0 < i:
                lu = board.board[i-1][j-1]
                if lu is not None:
                   moves.append(("Kill left up", i-1, j-1))
                   print(lu, 'on left up')

        return moves