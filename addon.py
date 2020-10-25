class Human:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    @staticmethod
    def run():
        print('I am running')

    @staticmethod
    def calc(*args):

        if len(args) <= 2:
            return args[0] + args[1]
        return 'Give me 2 numbers'

    @staticmethod
    def skip():
        print('I\'m skipping')
