import os
import pygame

black_king = pygame.image.load(os.path.join('assets', 'black-king.png'))
black_queen = pygame.image.load(os.path.join('assets', 'black-queen.png'))
black_bishop = pygame.image.load(os.path.join('assets', 'black-bishop.png'))
black_knight = pygame.image.load(os.path.join('assets', 'black-knight.png'))
black_rook = pygame.image.load(os.path.join('assets', 'black-rook.png'))
black_pawn = pygame.image.load(os.path.join('assets', 'black-pawn.png'))

white_king = pygame.image.load(os.path.join('assets', 'white-king.png'))
white_queen = pygame.image.load(os.path.join('assets', 'white-queen.png'))
white_bishop = pygame.image.load(os.path.join('assets', 'white-bishop.png'))
white_knight = pygame.image.load(os.path.join('assets', 'white-knight.png'))
white_rook = pygame.image.load(os.path.join('assets', 'white-rook.png'))
white_pawn = pygame.image.load(os.path.join('assets', 'white-pawn.png'))

black_piece = [black_king, black_queen, black_bishop, black_knight, black_rook, black_pawn]
white_piece = [white_king, white_queen, white_bishop, white_knight, white_rook, white_pawn]

WHITE_PIECE = []
BLACK_PIECE = []

for img in black_piece:
    BLACK_PIECE.append(pygame.transform.scale(img, (80, 80)))

for img in white_piece:
    WHITE_PIECE.append(pygame.transform.scale(img, (80, 80)))
