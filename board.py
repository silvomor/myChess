import pygame
from piece import King, Queen, Bishop, Knight, Rook, Pawn

order = [Rook, Knight, Bishop, Queen ,King , Bishop, Knight, Rook]

class Board:
    def __init__(self, rows = 8, cols = 8):
        self.rows = rows
        self.cols = cols

        self.board = [[None for p in range(rows)] for _ in range(cols)]
        
        for b, piece in zip(range(rows), order):
            self.board[b][0] = piece(0, b, 'black')
        
        for b in range(rows):
            self.board[b][1] = Pawn(1, b, 'black')

        for w in range(rows):
            self.board[w][6] = Pawn(6, w, 'white')

        for w, piece in zip(range(rows), order):
            self.board[w][7] = piece(7, w, 'white')


    def putOnBoard(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    self.board[i][j].draw(win)

    def selectPiece(self, x, y):
        print("trying to select :", self.board[x][y])
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    self.board[i][j].selected = False

        self.board[x][y].selected = True
        # print('Success !!!', self.board[x][y], "is selected", '\n')