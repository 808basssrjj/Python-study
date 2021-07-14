class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, play_game):
        self.play_game = play_game

    @staticmethod
    def show_help():
        print("帮助僵尸进入房子")

    @classmethod
    def show_top_score(cls):
        print("历史最高分%d" % cls.top_score)

    def start_game(self):
        print("%s游戏开始了" % self.play_game)


# 1.查看游戏帮助
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.创建游戏对象
game = Game("小明")
game.start_game()
