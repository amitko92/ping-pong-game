import init
from game import Game


def main():
    game = Game(init.window_width, init.window_height)
    game.start()


if __name__ == "__main__":
    main()
