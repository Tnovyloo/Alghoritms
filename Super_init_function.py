class Organism:
    def live(self):
        print('I live')


class Thinker:
    def think(self):
        print('I think')


class Human(Organism, Thinker):
    def __init__(self):
        print('I am human')
        super().live()
        super().think()


alice = Human()