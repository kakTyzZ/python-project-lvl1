#!/usr/bin/env python
import random
from brain_games.cli import name
from brain_games.scripts.brain import run, welcome


welcome()
name = name()


print('Answer "yes" if number even otherwise answer "no".')

right_answer = ["yes", "yes", "yes"]
question = []


def random_num():
    for i in range(3):
        num = random.randint(1, 20)
        question.append(num)


random_num()
print(question)


run(right_answer=right_answer, question=question, name=name)


def main():
    pass


if __name__ == "__main__":
    main()
