"""
Main entry point
"""

from game import Game

WIDTH = 200
HEIGHT = 150


def main():
    """
    Main function runs the main game loop
    """
    game = Game(height=HEIGHT, width=WIDTH)
    game.assign_random()
    game.game_loop()


if __name__ == "__main__":
    main()
