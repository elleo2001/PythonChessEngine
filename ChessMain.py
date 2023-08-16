"""
-Arquivo principal. 
-Ele é responsável por lidar com o input do usuário e fazer o display do objeto GameState decorrente.
"""

import pygame as p

import ChessEngine

p.init() # Inicia o pygame
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # Para animações
IMAGES = {}

'''
-Inicializa um dictionary de imagens. Será chamado exatamente uma vez no main.
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE)) # For loop para carregar as imagens / Definir altura e largura das imagens
    # Nota: é possível acessar uma imagem através de 'IMAGES['wp']' por exemplo

'''
-Parte principal do código.
-Lida com: Input de usuário e atualização de gráficos.
'''

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #

    loadImages()
    running = True
    sqSelected = () # Nenhum quadrado é selecionado, ele apenas rastreia o último clique do usuário (tuple: (row, col))
    playerClicks = [] # Mantem rastreado os cliques do jogador (duas tuples: [(6,4), (4,4)]) 
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) localização do mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                sqSelected = (row, col)
                if sqSelected == (row, col): # se o usuário clicar duas vezes no mesmo quadrado
                    sqSelected = () # deselecionar
                    playerClicks = [] # limpar o click do jogador
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append para ambos os primeiro e segundo cliques
                    if len(playerClicks) == 2:
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        if move in validMoves:
                            gs.makeMove(move)
                            moveMade = True
                        sqSelected = () # reseta o click do usuário
                        playerClicks = []
                
                # key handlers
                    elif e.type == p.KEYDOWN:
                        if e.key == p.K_z: # desfaz quando 'z' é precionado
                            gs.undoMove()
                            moveMade = True
            if moveMade:
                validMoves = gs.getValidMoves()
                moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
-Responsável por todos os gráficos no decorrer do jogo.
'''

def drawGameState(screen, gs):
    drawBoard(screen) # Desenhar os quadrados no tabuleiro
    # Adicionar highlighting nas peças ou sugestões de movimento
    drawPieces(screen, gs.board) # Desenhar as peças em cima dos quadrados


'''
-Desenha os quadrados no tabuleiro. O quadrado do topo a esquerda é sempre branco.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
-Desenha as peças no tabuleiro usando o atual GameState.board
'''

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #não for um quadrado vazio
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))   

if __name__ == "__main__":
    main()