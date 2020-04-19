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

        sqr = int(math.sqrt(n)) + 1

        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return "no"
        return "yes"

    def wrong():
        return print("You are wrong!")
    times_played = 0
    right_answer = 0
    while times_played < 3:
        num = random.randint(2, 500)
        print(f"Question:{num}")
        user_answer = prompt.string("Your answer: ")

        right_ans = is_prime(num)
        if user_answer == right_ans:
            correct()
            times_played += 1
            right_answer += 1
        elif user_answer != right_ans:
            wrong()
            times_played += 1
        else:
            invalid()
        if right_answer == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
