"""
Tic Tac Toe Player
"""
import sys
sys.setrecursionlimit(4000)
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    numx = 0
    numo = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == X:
                numx = numx + 1
            elif board[x][y] == O:
                numo = numo + 1
            else:
                pass
    if numx > numo:
        return O
    else:
        return X
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                moves.append([i, j])
            else:
                pass
    return moves
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):

    #deepcopy = copy.deepcopy(board)

    boardafterres = board

    boardafterres[action[0]][action[1]] = player(board)

    #board = deepcopy

    return boardafterres


    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):

    for i in range(len(board)):
        if all(board[i]) == X:
            winner_id = X
            return winner_id
        if all(board[i]) == O:
            winner_id = O
            return winner_id
    if board[0][1] == board[2][1] == board[1][1] == X:
        winner_id = X
        return winner_id
    if board[0][1] == board[2][1] == board[1][1] == O:
        winner_id = O
        return winner_id
    if board[0][2] == board[2][2] == board[1][2] == X:
        winner_id = X
        return winner_id
    if board[0][2] == board[2][2] == board[1][2] == O:
        winner_id = O
        return winner_id
    if board[0][0] == board[2][0] == board[1][0] == X:
        winner_id = X
        return winner_id
    if board[0][0] == board[2][0] == board[1][0] == O:
        winner_id = O
        return winner_id
    if board[0][0] == board[2][2] == board[1][1] == X:
        winner_id = X
        return winner_id
    if board[1][1] == board[2][2] == board[0][0] == O:
        winner_id = O
        return winner_id
    if board[0][2] == board[1][1] == board[2][0] == X:
        winner_id = X
        return winner_id
    if board[0][2] == board[1][1] == board[2][0] == O:
        winner_id = O
        return winner_id
    else:
        winner_id = None
        return winner_id

    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):

    a = []
    for i in range(len(board)):
        if EMPTY in board[i]:
            a.append("false")
        else:
            a.append("true")
    if a.count("false") > 0 and winner(board) is None:
        b = False
    else:
        b = True
    return b

    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):

    deepcpy2 = copy.deepcopy(board)

    deepcpy1 = copy.deepcopy(board)

    best_action = []

    if board == initial_state():

        """ RANDOM CELL [0, 2] IS SELECTED IN CASE OF EMPTY BOARD"""

        return [0, 2]

    def Minvalu(board):

        """SELECTS THE OPTIMAL MOVE OF THE MINIMISING/SECOND PLAYER"""
        """V IS THE UTILITY (SCORE 0 OR 1 OR -1) OF THE BOARD"""
        """INITIAL VALUE OF V IS SET TO AN INAPPLICABLE VALUE, DURING THE PROCESS IT GETS SET TO APPROPRIATE VALUE"""
        v = 2
        """IGNORE ALL PRINT STATEMENT, THESE ARE FOR DEBUGGING"""
        print("min", board)

        if terminal(board):
            print("returned", utility(board))
            v = utility(board)
            return v

        else:
            """SAVE THE BEFORE-PICTURE OF THE BOARD FOR RESTORING AFTER A MOVE IS EVALUATED"""
            deepcpy = copy.deepcopy(board)
            print("POSSIBLE MOVES", actions(board))
            """FOR THE COUNT OF EMPTY SPACE IN THE INPUT BOARD, LOOP THE FOLLOWING"""
            for K in actions(board):
                """RESULT BOARD IS BOARD AFTER MAKING ONE OF POSSIBLE MOVES"""
                result_board = result(board, K)
                print("resulting board", result_board)
                """MINVALU FUNCTN IS USED TO SELECT THE OPTIMAL MOVE FOR THE MINIMISING/ SECOND PLAYER."""
                """MAXVALU FUNCTN IS CALLED SO THAT MINIMUM OF THE UTILITY OF THE RESULTING BOARD (AFTER MAXIMISING/ 
                FIRST PLAYER) CAN BE SELECTED"""
                v = min(v, Maxvalu(result_board))
                """SET THE BOARD BACK TO COPY SAVED EARLIER, BEFORE EVALUATING THE NEXT MOVE"""
                board = deepcpy
                print("back to DC", board)
                """IF UTILITY = -1(BEST FOR MINIMISER/ SECOND PLAYER) END THE LOOP BECAUSE BEST MOVE IS FOUND"""
                if v == -1:

                    break
        """RETURNS FINAL SCORE OF MINIMISER/ SECOND PLAYER"""
        return v

    def Maxvalu(board):

        """STRUCTURE OF THIS FUNCTN IS EXACTLY LIKE THE MINVALU FUNCTION, HENCE COMMENTS WILL BE THE SAME.
        ONLY DIFFERENCES ARE COMMENTED BELOW"""

        v = -2

        print("max", board)

        if terminal(board):
            print("returned", utility(board))
            v = utility(board)
            return v

        else:
            deepcpy = copy.deepcopy(board)
            print("POSSIBLE MOVES", (actions(board)))
            for Z in actions(board):
                result_board = result(board, Z)
                print("resulting board", result_board)
                """MAXVALU FUNCTN IS USED TO SELECT THE OPTIMAL MOVE FOR THE MAXIMISING/ SECOND PLAYER."""
                """MINVALU FUNCTN IS CALLED SO THAT MINIMUM OF THE UTILITY OF THE RESULTING BOARD (AFTER MINIMISING/ 
                SECOND PLAYER) CAN BE SELECTED"""
                v = max(v, Minvalu(result_board))
                board = deepcpy
                print("back to DC", board)
                """IF V IS EQUAL TO 1, BREAK LOOP AS BEST MOVE IS FOUND"""
                if v == 1:
                    break

        return v

    if player(deepcpy2) == X:

        best_val = -1
        best_action = [-1, -1]

        for Y in actions(deepcpy2):
            """MAKES AN ARBITRARY MOVE AND CALLS THE SECOND PLAYER EVALUATOR(MINVALU FUNCTN)"""
            move_value = Minvalu(result(deepcpy2, Y))

            if move_value == 1:
                best_action = Y
                board = deepcpy2
                break
            if move_value > best_val:
                best_action = Y
                board = deepcpy2
        """RETURNS BEST POSSIBLE MOVE"""

    if player(deepcpy1) == O:

        best_val = 1

        best_action = [-1, -1]

        for S in actions(deepcpy1):
            """MAKES AN ARBITRARY MOVE AND CALLS THE FIRST PLAYER EVALUATOR(MAXVALU FUNCTN)"""
            move_value = Maxvalu(result(deepcpy1, S))
            if move_value == -1:
                best_action = S
                board = deepcpy1
                break
            if move_value < best_val:
                best_action = S
                board = deepcpy1
        """RETURNS BEST POSSIBLE MOVE"""


    return best_action

    raise NotImplementedError
