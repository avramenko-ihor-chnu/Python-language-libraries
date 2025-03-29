class Bird(object):
    def fly(self):
        print('I am flying.')
class Horse(object):
    def run(self):
        print('I am running.')

class Pegasus(Horse, Bird): pass

def main():
    bird = Bird()
    horse = Horse()
    pegasus = Pegasus()
    bird.fly()
    # bird.run() # помилка
    print()
    # horse.fly() # помилка
    horse.run(); print()
    pegasus.fly(); pegasus.run()
if __name__ == '__main__': main()
