#!/usr/bin/env python
import random
from brain_games.scripts.brain import run, welcome
from brain_games.cli import name


welcome()
name = name()
print("Find the greatest common divisor of given numbers.")


def main_data():
    data = {}
    while len(data) < 3:
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
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        data[nod(num1, num2)] = str(num1) + "," + str(num2)
    return data


data = main_data()
right_answer = list(data.keys())
question = list(data.values())


print(question, right_answer)

run(right_answer=right_answer, question=question, name=name)


def main():
    pass


if __name__ == "__main__":
    main()
