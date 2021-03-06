import pygame
import os
from board import Board

pygame.init()

board = pygame.image.load(os.path.join('assets', 'board01.png'))
BOARD = pygame.transform.scale(board, (640, 640))

WIDTH, HEIGHT = 640, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
rect = (7, 7, 637, 637)
WHITE = (255, 255, 255)
PIECE_HEIGHT, PIECE_WIDTH = 60, 40
FPS = 10
board1 = Board()

def redrawGameWindow():
    # global WIN, board1
    WIN.blit(BOARD, (0, 0))

    board1.putOnBoard(WIN, board1)

    pygame.display.update()

def click(pos):
    x, y = pos[0], pos[1]
    X, Y = int(x//(rect[2]/8)), int(y//(rect[2]/8))
    # print("\n\nCurrent Indices: ", Y, X)
    return (X, Y)

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        redrawGameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                j, i = click(pos)
                board1.selectPiece(i, j)
                redrawGameWindow()
                # try:
                #     board1.selectPiece(i, j)
                # except Exception as error:
                #     print('Error !', error)

                # prints the selected piece:  print(board1.board[i][j])
    del board1.board
    pygame.quit()

if __name__ == "__main__":
    main()