class GameView:
    def __init__(self):
        self.controller = GameController()

    def __display_menu(self):
        print("1)开始新游戏")
        print("2)退出游戏")

    def __select_menu(self):
        item= input("请选择")
        if item == "1":
            self.__move_action()
            self.__show_game()
        elif item == "2":
            return False
    def main(self):
        while True:
            self.__display_menu()
            if self.__select_menu() == False:
                break

    def __move_action(self):
        while True:
            item = input("请输入移动方向:l(左)|r(右)|u(上)|d(下)|q(退出):")
            if item == "l":
                self.controller.move_left()
                self.__show_game()
            elif item == "r":
                self.controller.move_right()
                self.__show_game()
            elif item == "u":
                self.controller.move_up()
                self.__show_game()
            elif item == "d":
                self.controller.move_down()
                self.__show_game()
            elif item == "q":
                break
    def __show_game(self):
        for r in self.controller.map:
            for c in r:
                print(c, end=" ")
            print()


class GameController:
    def __init__(self):
        self.__list_merge = []
        self.__map = [
                    [2, 0, 0, 2],
                    [4, 2, 0, 2],
                    [2, 4, 2, 4],
                    [0, 4, 0, 4],
                   ]
    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        for line in self.__map:
            self.__list_merge = line
            self.__merge()


    def move_right(self):
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge
    def square_matrix_transposition(self):

        for c in range(1, len(self.__map)):  # 1 2 3
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]
    def move_up(self):
        self.square_matrix_transposition()
        self.move_left()
        self.square_matrix_transposition()


    def move_down(self):
        self.square_matrix_transposition()
        self.move_right()
        self.square_matrix_transposition()

view = GameView()
view.main()