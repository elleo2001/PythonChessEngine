"""
-Esta clase é responsável por guardar toda a informação sobre a partida decorrente.
-Ela também será responsável por determinar os movimentos válidos conforme a partida se desenvolve.
-Também ira fazer um log dos movimentos.
"""
class GameState():
    def __init__(self):
        # O tabuleiro é uma lista 2d 8x8, cada elemento da lista tem dois caracteres.
        # O primeiro caractere representa a cor da peça, "b"(black(preto)) ou "w"(white(branco)).
        # O segundo caractere representa o tipo da peça, "K"(King(Rei)), "Q"(Queen(Rainha)), "p(pawn(peão))", etc.
        # "--" - representa uma casa sem nenhuma peça.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bK", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wK", "wR"]]
        self.moveFunction = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
                             'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}
        
        self.whiteToMove = True # Determina de quem é a vez a jogar.
        self.moveLog = [] # Armaneza os movimentos jogados.


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
             self.board[move.endRow][move.endCow] = move.pieceCaptured
             self.whiteToMove = not self.whiteToMove # troca de turnos de volta

    """
    
    """
    def getValidMoves(self):
        return self.getAllPossibleMoves() # Por enquanto sem me preocupar com cheques

    """
    
    """
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): # Numero de linhas
            for c in range(len(self.board[r])): # Numero de colunas em determinada linha
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves) #
            return moves


    """

    """
    def getPawnMoves(self, r, c, moves):
        pass
        if self.whiteToMove: # movimentos do peão branco
            if self.board[r-1][c] == "--": #
                moves.append(Move(r, c), (r-1, c), self.board)
                if r == 6 and self.board[r-2][c] == "--": #
                    moves.append(Move(r, c), (r-2, c), self.board)
            if c-1 >= 0: # 
                if self.board[r-1][c-1][0] == 'b': # peça inimiga para se capturar
                    moves.append(Move(r, c), (r-1, c-1), self.board)
            if c+1 < 7: #
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r, c), (r-1, c+1), self.board))

        else: # movimentos do peão preto
            if self.board[r + 1][c] == "--": # movimento de uma casa
                moves.append(Move((r, c), (r +1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "--": # movimento de duas casas
                    moves.append(Move((r, c), (r + 2, c), self.board))
            # capturas
            if c - 1 >= 0: # captura para a esquerda
                if self.board[r + 1][c - 1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 <= 7: # captura para a direita
                if self.board[r + 1][c + 1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))
        # adicionar promoções de peão depois
    
    """
    Pega todos os movimento para a torre localizados na linha, coluna e adiciona esses movimentos na lista
    """

    def getRookMoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) # cima, esquerda, baixo e direita
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol <8: # assegurar que está no tabuleiro
                    endPiece = self.board[endRow[endCol]]
                    if endPiece == "--": # espaço vazio válido
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor: # peça inimiga válida
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break
                else: # peça amigável inválida
                    break
            else: #sair do tabuleiro
                break
    
    

    def getKnightMoves(self, r, c, moves):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1), )
        pass

    
    
    

    def getBishopMoves(self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) # 4 diagonais
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8): # bispo pode se mover no máximo 7 casas
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: # assegurar que está no tabuleiro
                    endPiece = self.board[endRow][endCol] # se estiver no tabuleiro, eu pego a peça para se:  
                    if endPiece == "--": # é uma casa vazia
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor: # ou uma peça inimiga
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break
                    else: #
                        break
                else:
                    break
        

    
    
    """

    def getQueenMoves(self, r, c, moves):
        pass

    """

    def getKingMoves(self, r, c, moves):
        pass

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
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
    
    """

    """
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]