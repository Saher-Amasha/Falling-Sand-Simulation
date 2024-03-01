from game import Game

WIDTH =200
HEIGHT = 150

def main():
    game=Game(height=HEIGHT,width=WIDTH)
    game.assign_random()
    game.game_loop()

if __name__ == "__main__":
    main()