from tictactoe.board import Board
from itertools import cycle


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players

    def _check(self):
        """
           If the game ends return True, else False
        """
        pass

    def run(self):
        for player in cycle(self._players):
            move = player.move()
            self._board.board = move
            if self.check():
                return
