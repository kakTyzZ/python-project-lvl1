import prompt
from brain_games.scripts.brain import welcome


def name():
    name = prompt.string('May i have your name? ')
    return name


print(welcome())

name = name()


if __name__ == "__main__":
    name()
