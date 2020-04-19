#!/usr/bin/env python
import random
from .brain_even import correct
from brain_games.cli import name
import prompt
from .brain_calc import invalid


def nod(a, b):
    # Check the lowest number
    if a < b:
        x = a
    else:
        x = b
    # Add numbers to a list
    l1 = []
    for i in range(x):
        l1.append(i + 1)
    l2 = l1[::-1]
    for i in l2:
        if a % i == 0 and b % i == 0:
            return i
            break


def main():
    def wrong():
        return print("You are wrong!")
    print(f"Hello,{name}!")
    print("Find the greatest common divisor of given numbers.")
    times_played = 0
    answer = 0
    while times_played < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        right_answer = nod(num1, num2)
        print(f"question: {num1},{num2}")
        user_answer = prompt.integer("Your answer: ")
        if right_answer == user_answer:
            correct()
            times_played += 1
            answer += 1
        elif user_answer != right_answer:
            wrong()
            times_played += 1
        else:
            invalid()
        if answer == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
