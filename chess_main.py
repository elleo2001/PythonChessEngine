"""
-Arquivo principal. 
-Ele é responsável por lidar com o input do usuário e fazer o display do objeto GameState decorrente.
"""

import pygame as p
from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # Para animações
IMAGES = {}

'''
-Inicializa um dictionary de imagens. Será chamado exatamente uma vez no main.
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bK', 'bR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Nota: é possível acessar uma imagem através de 'IMAGES['wp']'

'''
-Parte principal do código.
-Lida com: Input de usuário e atualização de gráficos.
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(scree, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
-Responsável por todos os gráficos no decorrer do jogo.
'''

def drawGameState(screen, gs):
    drawBoard(screen) # Desenhar os quadrados no tabuleiro
    # Adicionar highlighting nas peças ou sugestões de movimento
    drawPieces(screen, gs.board) # Desenhar as peças em cima dos quadrados

if __name__ == "__main__":
    main()