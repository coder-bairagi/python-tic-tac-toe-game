class TicTacToe:
    def __init__(self, player1, player2, isComputerPlayer=False) -> None:
        from os import system
        import random
        self.gameTitle = "TIC TAC TOE"
        self.player1 = player1
        self.player2 = player2
        self.isComputerPlayer = isComputerPlayer
        self.title = f'Player 1: {self.player1} [ X ]\t\tPlayer 2: {self.player2} [ O ]'
        self.board = [i for i in range(1, 10)]
        self.winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        # formulation of leftIndent -> (length of title // 2) + 1 - ((11 // 2) + 1) where 11 is the fixed board's width
        self.titleBarLength = len(self.title)
        self.titleBarLength = self.titleBarLength if self.titleBarLength % 2 == 0 else self.titleBarLength + 1
        self.boardLeftIndent = (self.titleBarLength - 7) // 2
        self.clearConsole = lambda: system('cls')
        self.random = random

    def printTitle(self):
        playerNames = self.player1 + self.player2
        borderLength = len(self.title) + 10
        border = '-' * borderLength
        paddingLeft = ' ' * ((borderLength - len(self.gameTitle) - 2) // 2)
        paddingRight = ((borderLength - len(self.gameTitle) - 2) // 2)
        paddingRight = ' ' * (paddingRight if len(playerNames) % 2 != 0 else paddingRight + 1)
        paddingY = ' ' * (borderLength - 2)
        print(border)
        print(f'|{paddingY}|')
        print(f'|{paddingLeft}{self.gameTitle}{paddingRight}|')
        print(f'|{paddingY}|')
        print(border)
        print(f'\n{self.title}\n')

    def printBoard(self):
        print(f'{' '*self.boardLeftIndent} {self.board[0]} | {self.board[1]} | {self.board[2]} ')
        print(f'{' '*self.boardLeftIndent}---|---|---')
        print(f'{' '*self.boardLeftIndent} {self.board[3]} | {self.board[4]} | {self.board[5]} ')
        print(f'{' '*self.boardLeftIndent}---|---|---')
        print(f'{' '*self.boardLeftIndent} {self.board[6]} | {self.board[7]} | {self.board[8]} ')

    def isOpted(self, choice):
        return True if isinstance(self.board[choice - 1], str) else False
            

    def updateBoard(self, turn, choice):
        if self.isOpted(choice):
            return False
        if turn == 1:
            self.board[choice - 1] = 'X'
        elif turn == 0:
            self.board[choice - 1] = 'O'
        return True

    def checkWin(self):
        for win in self.winConditions:
            if self.board[win[0]] == self.board[win[1]] and self.board[win[1]] == self.board[win[2]] and self.board[win[0]] == self.board[win[2]]: 
                return True
        return False

    def checkDraw(self):
        counter = 0
        for box in self.board:
            if not isinstance(box, int):
                counter += 1
        if counter == 8:
            return True
        return False

    def printWinDrawMessage(self, winText):
        borderLength = len(winText) + 10
        border = '-' * borderLength
        paddingX = ' ' * 4
        paddingY = ' ' * (borderLength - 2)
        print(border)
        print(f'|{paddingY}|')
        print(f'|{paddingX}{winText}{paddingX}|')
        print(f'|{paddingY}|')
        print(border)
        print()

    def computerMove(self):
        availableMoves = [i for i in range(1, 10) if not self.isOpted(i)]
        return self.random.choice(availableMoves)

    def main(self):
        print()
        self.printTitle()
        self.printBoard()
        print()
        turn = 1
        while True:
            if (turn == 1) or (turn == 0 and not self.isComputerPlayer):
                while True:
                    if turn == 1:
                        choice = input(f'{self.player1}\'s turn: ')
                        choice = int(choice) if choice.isdigit() else 45
                    else:
                        choice = input(f'{self.player2}\'s turn: ')
                        choice = int(choice) if choice.isdigit() else 45
                    if 1 <= choice <= 9:
                        break
                    else:
                        print('\nPlease Enter a value between 1 to 9')
            else:
                print(f'{self.player2}\'s turn (Computer):') # Computer's turn
                choice = self.computerMove()
            
            if not self.updateBoard(turn, choice):
                print(f'\n{choice} is already opted, please select any other box')
                continue
            self.clearConsole()
            print()
            self.printTitle()
            self.printBoard()
            print()
            if self.checkWin() and turn == 1:
                self.printWinDrawMessage(f'Congratulations {self.player1}. You Won!')
                break
            elif self.checkWin() and turn == 0:
                self.printWinDrawMessage(f'Congratulations {self.player2}. You Won!')
                break
            elif self.checkDraw():
                self.printWinDrawMessage(f'It\'s a Draw')
                break
            turn = 1 - turn

    def run(self):
        self.main()
        print()
        input("Press Any Key to exit...")
        print()


if __name__ == '__main__':
    gameMode = input("\nChoose mode:\n1 for Player vs Player\n2 for Player vs Computer: ").strip()
    player1 = input("\nPlease Enter Player 1 Name: ").strip()
    player2 = "Computer" if gameMode == '2' else input("Please Enter Player 2 Name: ").strip()
    ticTacToe = TicTacToe(player1=player1, player2=player2, isComputerPlayer=(gameMode == '2'))
    ticTacToe.run()
