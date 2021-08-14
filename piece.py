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

    def draw(self, win, board):
        if self.color == "white":
            drawThis = WHITE_PIECE[self.img]
        else:
            drawThis = BLACK_PIECE[self.img]       

        x, y = self.col * round(self.rect[2]/8), self.row * round(self.rect[2]/8)
        # print(x, y,)

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 76, 76), 2)
        
            myMoves = self.validMoves(board)
            for aMove in myMoves:
                cx, cy = 40 + aMove[2] * round(self.rect[2]/8), 40 + aMove[1] * round(self.rect[2]/8)
                pygame.draw.circle(win, (255, 0, 0), (cx, cy), 10)
                pygame.draw.rect(win, (0, 0, 0), (cx-40+5, cy-40+5, 65, 65), 2)

        win.blit(drawThis, (x, y))

class King(Piece):
    img = 0
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j =  self.row, self.col
        print(i, j)
        moves =[]
        if self.color == 'white':
            pass
        elif self.color == 'black':
            pass
        return moves
        
class Queen(Piece):
    img = 1
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j =  self.row, self.col
        moves =[]

        # # ROOK LIKE MOVES
        # LONG JUMP UP
        if i > 0:
            for x in range(i-1, -1, -1):
                if board.board[x][j] is None:
                    moves.append(('safe move up', x, j))
                elif board.board[x][j] is not None:
                    # UP KILL MOVE
                    moves.append(('kill', x, j))
                    break
        # LONG JUMP DOWN
        if i < 7:
            for x in range(i+1, 8, 1):
                if board.board[x][j] is None:
                    moves.append(('safe move Down', x, j))
                elif board.board[x][j] is not None:
                    # DOWN KILL MOVE
                    moves.append(('kill', x, j))
                    break
        i, j =  self.row, self.col
        # LONG JUMP RIGHT
        if j < 7:
            for y in range(j+1, 8, 1):
                if board.board[i][y] is None:
                    moves.append(('safe move Right', i, y))
                elif board.board[i][y] is not None:
                    # RIGHT KILL MOVE
                    moves.append(('kill', x, j))
                    break
        # LONG JUMP LEFT
        if j > 0:
            for y in range(j-1, -1, -1):
                if board.board[i][y] is None:
                    moves.append(('safe move left', i, y))
                elif board.board[i][y] is not None:
                    # RIGHT KILL MOVE
                    moves.append(('kill', x, j))
                    break
        
        # HOLDING POSITIONS AGAIN IN X , Y
        x , y = i , j
        # print(x, y)
        # # BISHOP LIKE MOVES 
        # MARCH TOWARDS LEFT TOP CORNER
        while x > 0 and y > 0:
            x, y = x - 1, y - 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))
        # MARCH TOWARDS LEFT BOTTOM CORNER
        while x < 7 and y > 0:
            x, y = x + 1, y - 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))
        # MARCH TOWRDS RIGHT TOP CORNER
        while x > 0 and y < 7:
            x, y = x - 1, y + 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))   
        # MARCH TOWRDS RIGHT BOTTOM CORNER
        while x < 7 and y < 7:
            x, y = x + 1, y + 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))
        
        return moves

class Bishop(Piece):
    img = 2
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j =  self.row, self.col
        x, y = i, j
        # print(i, j)
        moves =[]
        # MARCH TOWARDS LEFT TOP CORNER
        while x > 0 and y > 0:
            x, y = x - 1, y - 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))
        # MARCH TOWARDS LEFT BOTTOM CORNER
        while x < 7 and y > 0:
            x, y = x + 1, y - 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))
        # MARCH TOWRDS RIGHT TOP CORNER
        while x > 0 and y < 7:
            x, y = x - 1, y + 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))   
        # MARCH TOWRDS RIGHT BOTTOM CORNER
        while x < 7 and y < 7:
            x, y = x + 1, y + 1
            if board.board[x][y]:
                moves.append(('kill', x, y))
                x, y = i, j
                break
            moves.append(('safe jump', x, y))
        
        return moves

class Knight(Piece):
    img = 3
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j =  self.row, self.col
        print(i, j)
        moves =[]
        if self.color == 'white':
            pass
        elif self.color == 'black':
            pass
        return moves

class Rook(Piece):
    img = 4
    def __str__(self) -> str:
        return self.color+ "-" + str(self.__class__.__name__)

    def validMoves(self, board):
        i, j =  self.row, self.col
        moves =[]
        # LONG JUMP UP
        if i > 0:
            for x in range(i-1, -1, -1):
                if board.board[x][j] is None:
                    moves.append(('safe move up', x, j))
                elif board.board[x][j] is not None:
                    # UP KILL MOVE
                    moves.append(('kill', x, j))
                    break
        # LONG JUMP DOWN
        if i < 7:
            for x in range(i+1, 8, 1):
                if board.board[x][j] is None:
                    moves.append(('safe move Down', x, j))
                elif board.board[x][j] is not None:
                    # DOWN KILL MOVE
                    moves.append(('kill', x, j))
                    break
        i, j =  self.row, self.col
        # LONG JUMP RIGHT
        if j < 7:
            for y in range(j+1, 8, 1):
                if board.board[i][y] is None:
                    moves.append(('safe move Right', i, y))
                elif board.board[i][y] is not None:
                    # RIGHT KILL MOVE
                    moves.append(('kill', x, j))
                    break
        # LONG JUMP LEFT
        if j > 0:
            for y in range(j-1, -1, -1):
                if board.board[i][y] is None:
                    moves.append(('safe move left', i, y))
                elif board.board[i][y] is not None:
                    # RIGHT KILL MOVE
                    moves.append(('kill', x, j))
                    break
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
        # print(i, j)
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

            # KILLING DIAGONAL PIECES
            if j < 7 and i < 7:
                rd = board.board[i+1][j+1]
                if rd is not None:
                   moves.append(("kill right down", i+1, j+1))

            if j > 0 and i < 7:
                ld = board.board[i+1][j-1]
                if ld is not None:
                   moves.append(("kill left down", i+1, j-1))

        # WHITE PAWNS
        elif self.color == 'white':
            f1 = board.board[i-1][j]
            # FIRST MOVE WITH TWO OPTIONS
            if self.first:
                f2 = board.board[i-2][j]

                if not f1:
                    moves.append(('safe single jump', i-1, j))
                    if not f2:
                        moves.append(('safe double jump', i-2, j))
            # NORMAL SINGLE STEP MOVE
            else:
                if not f1:
                    moves.append(('safe single jump', i-1, j))


            # KILLING DIAGONAL PIECES
            if j < 7 and 0 < i:
                ru = board.board[i-1][j+1]
                if ru is not None:
                   moves.append(("kill right up", i-1, j+1))

            if j > 0 and 0 < i:
                lu = board.board[i-1][j-1]
                if lu is not None:
                   moves.append(("kill left up", i-1, j-1))

        return moves