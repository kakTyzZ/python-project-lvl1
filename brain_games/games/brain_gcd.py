#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.brain import main

print("Find the greatest common divisor of given numbers.")

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


def random_num1():
    num1 = random.randint(1, 100)
    return num1
num1 = random_num1()
def random_num2():
    num2 = random.randint(1, 100)
    return num2
num2 = random_num2()
    


def gcd_answer(num1,num2):
    right_answer = nod(num1, num2)
    return right_answer  
right_answer1 = gcd_answer(num1,num2)




def question_num(num1,num2):
    num = str(num1) + "," + str(num2)
    return print(f"Question:{num}")
question = question_num(num1,num2)


print("test")


main(right_answer1)


if __name__ == "__main__":
    main()


