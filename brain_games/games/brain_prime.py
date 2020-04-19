#!/usr/bin/env python
import math
from .brain_even import correct
from brain_games.cli import name
import prompt
from .brain_calc import invalid
import random


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

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

    def wrong():
        return print("You are wrong!")
    TIMES_PLAYED = 0
    RIGHT_ANSWER = 0
    while TIMES_PLAYED < 3:
        num = random.randint(2, 500)
        print(f"Question:{num}")
        USER_ANSWER = prompt.string("Your answer: ")

        RIGHT_ANS = is_prime(num)
        if USER_ANSWER == RIGHT_ANS:
            correct()
            TIMES_PLAYED += 1
            RIGHT_ANSWER += 1
        elif USER_ANSWER != RIGHT_ANS:
            wrong()
            TIMES_PLAYED += 1
        else:
            invalid()
        if RIGHT_ANSWER == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
