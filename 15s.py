#reference sample
ref = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

class Game(list):
    def __init__(self):
        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.data = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                self.data[i].append(l.pop(random.randint(0, len(l)-1)))
        print("Game started!")

    def coord(self):
        for i in range(4):
            try:
                y = self.data[i].index(0)
            except:
                pass
            else:
                self.str = i
                self.col = y

    def left(self):
        self.coord()
        print("empty cell coordinates: (", self.str,";", self.col, ")")
        if self.col - 1 >= 0:
            self.data[self.str][self.col] = self.data[self.str][self.col - 1]
            self.data[self.str][self.col - 1] = 0
            print("Succeed! Move on!")
        else:
            print('Operation cannot be performed! Out of range')

    def up(self):
        self.coord()
        print("empty cell coordinates: (", self.str,";", self.col, ")")
        if self.str - 1 >= 0:
            self.data[self.str][self.col] = self.data[self.str - 1][self.col]
            self.data[self.str - 1][self.col] = 0
            print("Succeed! Move on!")
        else:
            print('Operation cannot be performed! Out of range')

    def right(self):
        self.coord()
        print("empty cell coordinates: (", self.str,";", self.col, ")")
        if self.col + 1 < 4:
            self.data[self.str][self.col] = self.data[self.str][self.col + 1]
            self.data[self.str][self.col + 1] = 0
            print("Succeed! Move on!")
        else:
            print('Operation cannot be performed! Out of range')

    def down(self):
        self.coord()
        print("empty cell coordinates: (", self.str,";", self.col, ")")
        if self.str + 1 < 4:
            self.data[self.str][self.col] = self.data[self.str + 1][self.col]
            self.data[self.str + 1][self.col] = 0
            print("Succeed! Move on!")
        else:
            print('Operation cannot be performed! Out of range')

    def m_print(self):
        print_matrix = ""
        for i in range(4):
            for j in range(4):
                if self.data[i][j]< 10:
                    item = " "+ str(self.data[i][j])
                else:
                    item = str(self.data[i][j])
                print_matrix = print_matrix + "| " + item
            print_matrix = print_matrix + "| " + "\n"
        print(print_matrix)

ref = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
answer = input("Would yo like to start a game? Please, enter Y/N: ")

if answer.lower() == 'y':
    m = Game()
    m.m_print()

while m != ref:
    action = input("Please, choose an action (left, right, up, down): ")
    if action == "left":
        m.left()
        m.m_print()
    elif action == "right":
        m.right()
        m.m_print()
    elif action == "up":
        m.up()
        m.m_print()
    elif action == "down":
        m.down()
        m.m_print()
    elif action == "q":
        break
else:
    print("Congrats! Game over!")