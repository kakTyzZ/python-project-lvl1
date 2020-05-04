#!/usr/bin/env python
import random
from brain_games.cli import name
from brain_games.scripts.brain import run, welcome


welcome()
print("What number is missing in the progression")
name = name()

question = []
right_answer = []


def random_progression():
    for i in range(3):
        start_num = random.randint(1, 10)
        step = random.randint(1, 10)
        listt = []
        listt.append(start_num + step)
        for i in range(9):
            num = listt[-1]
            listt.append(num + step)
        random_num = random.randint(1, 9)
        pop_num = listt.pop(random_num)
        listt.insert(random_num, "..")
        question.append(tuple(listt))
        right_answer.append(pop_num)


random_progression()


run(right_answer=right_answer, question=question, name=name)


def main():
    pass


if __name__ == "__main__":
    main()
