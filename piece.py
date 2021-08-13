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
        i, j =  self.col, self.row
        print(i, j)
        moves = []

        if self.color == 'black':
            if self.first:
                p1, p2 = board.board[i+1][j], board.board[i+2][j]
                print(p1, p2)
                if not p1:
                    moves.append(('safe single jump', i+1, j))
                    if not p2:
                        moves.append(('safe double jump', i+2, j))

        elif self.color == 'white':
            if self.first:
                p1, p2 = board.board[j][i-1], board.board[j][i-2]
                print(p1, p2)
                if not p1:
                    moves.append(('safe single jump', i-1, j))
                    if not p2:
                        moves.append(('safe double jump', i-2, j))


        return moves