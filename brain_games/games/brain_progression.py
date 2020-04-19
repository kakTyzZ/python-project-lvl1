#!/usr/bin/env python
import random
from .brain_even import correct
from brain_games.cli import name
import prompt
from .brain_calc import invalid


def random_progression():
    start_num = random.randint(1, 10)
    step = random.randint(1, 10)
    listt = []
    listt.append(start_num + step)
    for i in range(9):
        num = listt[-1]
        listt.append(num + step)
    return listt


def main():
    print(f"Hello,{name}!")
    print("What number is missing in the progression?")

    def wrong():
        return print("You are wrong!")
    times_played = 0
    answer = 0
    while times_played < 3:
        list1 = random_progression()
        random_num = random.randint(1, 9)
        pop_num = list1.pop(random_num)
        list1.insert(random_num, "..")
        print(f"Question: {list1}")
        user_answer = prompt.integer("Your answer: ")
        if user_answer == pop_num:
            correct()
            times_played += 1
            answer += 1
        elif user_answer != pop_num:
            wrong()
            times_played += 1
        else:
            invalid()
        if answer == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
