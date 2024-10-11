import random
import pdb
from os import system
from enum import Enum


class GameStatus(Enum):
    PLAYING = 0
    LOSE = 1
    WIN = 2

class MineBoard(object):

    def __init__(self, w, h, k):
        # Create a new board with size w x h
        self.w = w
        self.h = h
        self.board = [[0 for i in range(w)] for j in range(h)]
        self.allocateMines(w, h, k)
        self.status = GameStatus.PLAYING
        self.cellsToOpen = w * h - k

    def allocateMines(self, w, h, numOfMines):
        allocIndexes = self.getRandomPos(w * h, numOfMines)
        for i in allocIndexes:
            self.setMine(int(i / w), i % h)
            self.setAdjacentMines(int(i / w), i % h)

    def printLayout(self):
        print(' ' * 7 + ''.join(map(lambda x : '{:^7d}'.format(x + 1), range(self.w))))
        print(' ' * 7 + '-' * (self.w * 7))
        for (i, row) in enumerate(self.board):
            print('{:^7d}'.format(i + 1) + '|' + ' |'.join(list(map(lambda x : '{:^5s}'.format(self.display(x)), row))) + ' | ')
            print(' ' * 7 + '-' * (self.w * 7))

    def click(self, row, col):
        value = self.reveal(row, col)
        if value:
            self.cellsToOpen -= 1
            if self.cellsToOpen == 0:
                self.status = GameStatus.WIN
            if self.hasMine(row, col):
                self.status = GameStatus.LOSE
            elif self.isBlank(row, col):
                for dr in range(row - 1, row + 2):
                    for dc in range(col - 1, col + 2):
                       self.click(dr, dc)

    def flag(self, row, col):
        if self.isValidCell(row, col) and self.isHidden(row, col):
            self.toggleFlag(row, col)

    def isValidCell(self, row, col):
        return row >= 0 and row < self.h and col >= 0 and col < self.w


    def getRandomPos(self, n, k):
        res = []
        remains = [i for i in range(n)]
        while k > 0:
            r = random.randint(0, len(remains) - 1)
            res.append(r)
            del remains[r]
            k -= 1
        return res

    #Convention for cell values:
    #    - 0 : Hidden Blank
    #    - 10 : Revealed Blank
    #    - -1 : Hidden Bomb
    #    - 9 : Revealed Bomb
    #    - 1 ~ 8 : number of adjacent bomb (hidden)
    #    - 11 ~ 18 : adjacent bomb (revealed)
    #    - x + 100 : Flagged
    #

    def setMine(self, row, col):
        self.board[row][col] = -1

    def setAdjacentMines(self, row, col):
        for dr in range(row - 1, row + 2):
            for dc in range(col - 1, col + 2):
                if self.isValidCell(dr, dc) and not self.hasMine(dr, dc):
                    self.board[dr][dc] += 1

    def toggleFlag(self, row, col):
        if self.isFlagged(row, col):
            self.board[row][col] -= 100
        else:
            self.board[row][col] += 100

    # Open a cell and return its value
    def reveal(self, row, col):
        if not self.isValidCell(row, col) or not self.isHidden(row, col):
            return None
        if self.isFlagged(row, col):
            self.toggleFlag(row, col)
        self.board[row][col] += 10
        return self.board[row][col]

    def isHidden(self, row, col):
        return self.board[row][col] < 9

    def hasMine(self, row, col):
        return self.board[row][col] % 10 == 9

    def isBlank(self, row, col):
        return self.board[row][col] % 10 == 0

    def isOver(self):
        return self.winGame() or self.loseGame()

    def loseGame(self):
        return self.status == GameStatus.LOSE

    def winGame(self):
        return self.status == GameStatus.WIN

    def isFlagged(self, row, col):
        return self.board[row][col] > 90

    def revealAll(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.reveal(i, j)

    def display(self, ip):
        if ip > 90:
            return 'F'
        elif ip == 9:
            return '*'
        elif ip == 10:
            return '.'
        elif ip > 10:
            return str(ip - 10)
        return ''


def cls():
    system('clear')

def play():
    w = int(input('Enter width of board: '))
    h = int(input('Enter height of board: '))
    m = int(input('Enter number of mines : '))
    while m >= w * h - 1:
        m = int(input('Too many mines. Enter again : '))
    game = MineBoard(w, h, m)
    while not game.isOver():
        cls()
        game.printLayout()
        command = nextCommand()
        splits = command.split(' ')
        row = int(splits[0]) - 1
        col = int(splits[1]) - 1
        if command[-1] == 'F':
            game.flag(row, col)
        else:
            game.click(row, col)

    game.revealAll()
    cls()
    game.printLayout()
    if game.loseGame():
        print('You lose !!')
    elif game.winGame():
        print('You win !!. Congradulations !!')


def nextCommand():
    instruction = 'Commands : \n<row> <col> : open cell\n<row> <col> F : flag cell\nq : quit\n'
    return input(instruction).strip()

play()