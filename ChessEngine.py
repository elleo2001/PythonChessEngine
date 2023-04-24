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


    """
    -Recebe um movimento como parâmetro e o executa (isso não irá funcionar para roque, promoção de peão e en passant)
    """
    def makeMove(self, move):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move) # Fazer o log do movimento, para que seja possível desfazer depois
            self.whiteToMove = not self.whiteToMove #Trocar jogadores

    """
    -Desfaz o último movimento feito
    """

    def undoMove(self):
        if len(self.moveLog) != 0: # tem certeza que há um movimento a se desfazer
             move = self.moveLog.pop()
             self.board[move.startRow][move.startCol] = move.pieceMoved
             self.board[move.endRow][move.endRow] = move.pieceCaptured
             self.whiteToMove = not self.whiteToMove # troca de turnos de volta

class Move():
    # mapeia chaves para valores
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]