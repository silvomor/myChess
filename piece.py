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
    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []
        # TOP MOVES
        

class Queen(Piece):
    img = 1
    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []

class Bishop(Piece):
    img = 2
    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []

class Knight(Piece):
    img = 3
    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []

        # DOWN LEFT
        if i < 6 and j > 0:
            _ = board[i+2][j-1]
            if _ is None:
                moves.append((i+2, j-1))
        # DOWN RIGHT
        if i < 6 and j < 7:
            _ = board[i+2][j+1]
            if _ is None:
                moves.append((i+2, j+1))
        # UP LEFT
        if i < 6 and j > 0:
            _ = board[i+2][j+1]
            if _ is None:
                moves.append((i+2, j+1))
        # UP RIGHT
        if i < 6 and j < 7:
            _ = board[i+2][j+1]
            if _ is None:
                moves.append((i+2, j+1))
        return moves

class Rook(Piece):
    img = 4
    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []

class Pawn(Piece):
    img = 5
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False

    def validMoves(self, board):
        i, j = self.row, self.col
        moves = []

        if i < 7:
            # FORWARD 2
            if self.first:
                _ = board[i+1][j]
                if _ is None:
                    moves.append((i+2, j))
            # FORWARD 1
            else:
                _ = board[i+1][j]
                if _ is None:
                    moves.append((i+1, j))
        return moves