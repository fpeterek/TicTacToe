import os

def char_in_string(char, string):
    return char in string

def check_number(char):
    return char_in_string(char, '123')

def check_letter(char):
    return char_in_string(char, 'ABC')

def letter_to_num(char):
    m = { 'A' : '1', 'B' : '2', 'C' : '3' }
    return m[char]

def clear():
    # os.name is nt on windows
    # cls clears console on windows, clear on unix
    # if os is not windows, call clear, otherwise call cls
    os.system("clear" if os.system != "nt" else "cls")

class TicTacToe:

    __board = []
    __active_player = 0

    def __init__(self):
        self.__reset()

    def __draw(self):
        clear()
        print("     A | B | C")
        numbers = ['1', '2', '3']
        for i in range(len(self.__board)):
            print("   -------------")
            print(" " * 10)
            print(numbers[i], " | ", end="")
            print(self.__board[i][0], "|", self.__board[i][1], "|", self.__board[i][2], "|")
            print(" " * 10)
        print("   -------------")
        print(" " * 10)

    def __check_input(self, string):
        string = string.upper()
        if len(string) != 2:
            raise Exception()
        char_found = False
        letter = ''
        number = ''
        if check_letter(string[0]):
            char_found = True
            letter = string[0]
        else:
            if not check_number(string[0]):
                raise Exception()
            number = string[0]

        if char_found:
            if not check_number(string[1]):
                raise Exception()
            number = string[1]
        else:
            if not check_letter(string[1]):
                raise Exception()
            letter = string[1]
        return (number, letter)

    def __get_input(self):
        while True:
            coordinates = input("Player" + str(self.__active_player + 1) + ": ")
            x, y = 0, 0
            try:
                t = self.__check_input(coordinates)
                x, y = t[0], t[1]
                y = letter_to_num(y)
            except:
                self.__draw()
                print("Invalid coordinates")
                continue
            x = int(x) - 1
            y = int(y) - 1
            chars = "ox"
            if self.__board[x][y] != ' ':
                self.__draw()
                print("Square is already occupied")
                continue
            break
        self.__board[x][y] = chars[self.__active_player]
        self.__active_player ^= 1

    def __reset(self):
        clear()
        self.__board = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] ]
        self.__active_player = 0

    def __player_won(self, player_name):
        self.__draw()
        print(player_name, "won")
        input("Press enter to continue")
        self.__reset()

    def __tie(self):
        self.__draw()
        print("Game ends in a tie")
        input("Press enter to continue")
        self.__reset()

    def __check_rows(self):
        players = { 'o':'Player1', 'x':'Player2' }
        for i in (self.__board):
            if i[0] == i[1] and i[0] == i[2] and i[0] != ' ':
                self.__player_won(players[i[0]])
                return True
        return False

    def __check_columns(self):
        players = { 'o':'Player1', 'x':'Player2' }
        for i in [0, 1, 2]:
            if self.__board[0][i] == self.__board[1][i] and self.__board[0][i] == self.__board[2][i] and self.__board[0][i] != ' ':
                self.__player_won(players[self.__board[0][i]])
                return True
        return False

    def __check_diagonally(self):
        players = { 'o':'Player1', 'x':'Player2' }
        if self.__board[0][0] == self.__board[1][1] and self.__board[0][0] == self.__board[2][2] and self.__board[0][0] != ' ':
            self.__player_won(players[self.__board[0][0]])
            return True
        if self.__board[0][2] == self.__board[1][1] and self.__board[0][2] == self.__board[2][0] and self.__board[0][2] != ' ':
            self.__player_won(players[self.__board[0][2]])
            return True
        return False

    def __check_for_tie(self):
        for i in self.__board:
            for f in i:
                if f == ' ':
                    return
        self.__tie()

    # I'm just bored, never actually do this, for the love of Guido van Rossum
    # Use self or this, like any other sane person
    def __check_for_victory(geralt_of_rivia):

        if geralt_of_rivia.__check_rows():
            return
        if geralt_of_rivia.__check_columns():
            return
        if geralt_of_rivia.__check_diagonally():
            return

        geralt_of_rivia.__check_for_tie()

    def __loop(self):
        while True:
            self.__draw()
            self.__get_input()
            self.__check_for_victory()

    def start(self):
        try:
            self.__loop()
        except KeyboardInterrupt:
            print("", "Bye", sep="\n")

if __name__ == '__main__':
    game = TicTacToe()
    game.start()
