#!/usr/bin/env python
import random
import prompt
from brain_games.cli import name


def wrong():
    return print(f"'yes' is wrong answer.Correct answer was 'no'.")


def correct():
    return print("Correct!")


def random_num():
    number = random.randint(1, 20)
    return number


def invalid():
    return print("You can type only 'yes' or 'no'!")


def main():
    print(f"Hello,{name}!")
    print('Answer "yes" if number even otherwise answer "no".')
    TIMES_PLAYED = 0
    RIGHT_ANSWER = 0
    while TIMES_PLAYED < 3:
        num = random_num()
        print("question: " + str(num))
        answer = prompt.string("Your answer: ")
        if answer.isdigit():
            invalid()
        elif num % 2 == 0 and answer == "yes":
            correct()
            TIMES_PLAYED += 1
            RIGHT_ANSWER += 1
        elif num % 2 == 1 and answer == "no":
            correct()
            TIMES_PLAYED += 1
            RIGHT_ANSWER += 1
        else:
            wrong()
            TIMES_PLAYED += 1
        if RIGHT_ANSWER == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
