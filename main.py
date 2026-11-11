from game.game import Game

game = Game()

game.setup()

game.is_running = True
while game.is_running:
	game.update()
