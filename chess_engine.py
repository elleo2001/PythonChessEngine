"""
-Esta clase é responsável por guardar toda a informação sobre a partida decorrente.
-Ela também será responsável por determinar os movimentos válidos conforme a partida se desenvolve.
-Também ira fazer um log dos movimentos.
"""
class GameState():
    def __init__(self):
        # O tabuleiro é uma lista 2d 8x8, cada elemento da lista tem dois caracteres.
        # O primeiro caractere representa a cor da peça, "b" ou "w".
        # O segundo caractere representa o tipo da peça, "K", "Q", "p", etc.
        # "--" - representa um espaço sem nenhuma peça.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bK", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wK", "wR"]]
        self.whiteToMove = True
        self.moveLog = []