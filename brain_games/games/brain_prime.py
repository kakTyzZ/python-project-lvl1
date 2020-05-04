#!/usr/bin/env python
import math
from brain_games.cli import name
import random
from brain_games.scripts.brain import run, welcome


welcome()

print('Answer "yes" if given number is prime. Otherwise answer "no".')

name = name()


def is_prime(n):
    if n == 2:
        return "yes"
    if n % 2 == 0 or n <= 1:
        return "no"

    SQR = int(math.sqrt(n)) + 1

    for divisor in range(3, SQR, 2):
        if n % divisor == 0:
            return "no"
    return "yes"


question = []
right_answer = []


def random_num():
    for i in range(3):
        num = random.randint(2, 500)
        question.append(num)
        right_answer.append(is_prime(num))


random_num()

run(right_answer=right_answer, question=question, name=name)


def main():
    pass


if __name__ == "__main__":
    main()
