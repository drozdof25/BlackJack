from blackjack import Game
def main():
    print('Добро пожаловать!')
    name = input('Введите имя: ')
    game = Game(name)
    again = None
    while again != 'n':
        game.play()
        again  = input('Ещё? (y/n):')
if __name__ == '__main__':
    main()