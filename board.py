import pygame
from piece import King, Queen, Bishop, Knight, Rook, Pawn

order = [Rook, Knight, Bishop, Queen ,King , Bishop, Knight, Rook]
seePieces = {'Rook':Rook, 'Knight': Knight,'Bishop': Bishop, 'Queen': Queen ,'King':King , 'Pawn': Pawn}

class Board:
    def __init__(self, rows = 8, cols = 8):
        self.rows = rows
        self.cols = cols
        self.selectHistory = []

        self.board = [[None for p in range(rows)] for _ in range(cols)]
        
        for b, piece in zip(range(rows), order):
            self.board[0][b] = piece(0, b, 'black')
        
        for b in range(rows):
            self.board[1][b] = Pawn(1, b, 'black')

        for w in range(rows):
            self.board[6][w] = Pawn(6, w, 'white')

        for w, piece in zip(range(rows), order):
            self.board[7][w] = piece(7, w, 'white')
        
        # PUT CUSTOM HARD CODED PIECES HERE
        # self.board[3][0] = Knight(3, 0, 'white')
        # self.board[1][7] = Knight(1, 7, 'white')
        # self.board[2][2] = Knight(2, 2, 'white')
        # self.board[6][6] = Knight(6, 6, 'black')

    def __del__(self):
        print('Deleting Board')

    def putOnBoard(self, win, board):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    self.board[i][j].draw(win, board)

    def selectPiece(self, x, y):
        print(f'Select History (stack): {self.selectHistory}')
        print(f'You Clicked on: {x, y}')

        # SELECTING FIRST PIECE
        if len(self.selectHistory) < 1:
            print("trying to select :", self.board[x][y])
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j]:
                        self.board[i][j].selected = False

            if self.board[x][y]:
                self.board[x][y].selected = True
                self.selectHistory.append((x, y))
                print(self.selectHistory)
                
                myMoves = self.board[x][y].validMoves(self)
                print("Possible Moves: ", myMoves, '\n')

            return self.board[x][y]

        # SELECTING SECOND POSTION, TARGET AND DESELECTING
        else:
            px, py = self.selectHistory[-1][0], self.selectHistory[-1][1]
            tx, ty = x, y

            print([(px, py), (tx, ty)])
            if self.board[px][py].isSelected():
                for aMove in self.board[px][py].validMoves(self):
                    if (aMove[1], aMove[2]) == (tx, ty):
                        self.thisIsMyMove((px, py), (tx, ty))
            self.deSelectPiece(px, py)
            self.deSelectPiece(tx, ty)
                        
    def thisIsMyMove(self, curPos, target):
        x1, y1, x2, y2 = curPos[0], curPos[1], target[0], target[1]

        fromPiece = self.board[x1][y1]

        if self.board[x2][y2]:
            for aNewPiece in seePieces:
                if type(fromPiece).__name__ == aNewPiece:
                    self.board[x2][y2] = seePieces[aNewPiece](x2, y2, fromPiece.color)

            self.board[x1][y1] = None
        else:
            for aNewPiece in seePieces:
                if type(fromPiece).__name__ == aNewPiece:
                    self.board[x2][y2] = seePieces[aNewPiece](x2, y2, fromPiece.color)

            self.board[x1][y1] = None

        self.showBoard()
        print(f'Piece from {curPos} was moved to {target}')

    def deSelectPiece(self, x, y):
        if self.board[x][y]:
            self.board[x][y].selected = False
        self.selectHistory = []

    def showBoard(self):
        currentBoard = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    currentBoard.append(type(self.board[i][j]).__name__ + '-' + self.board[i][j].color)
                else:
                    currentBoard.append(None)
        print(currentBoard)

    def promotePawn(self, pawnPiece):
        px, py = pawnPiece.row, pawnPiece.col
        print(pawnPiece, 'is trying to promote')
        self.board[px][py] = Queen(px, py, pawnPiece.color)
        pawnPiece = None
        pygame.display.update()

    def game(self):
        pass