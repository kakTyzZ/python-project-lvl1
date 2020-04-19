#!/usr/bin/env python
import random
import operator
import prompt
from .brain_even import correct
from brain_games.cli import name


def invalid():
    return print("You can type only numbers!")


opr = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def main():
    def wrong():
        return print(
            f"{answer} is wrong answer.Correct answer was {result}.\nLet\'s try again, {name} !")
    print(f"Hello,{name}!")
    print("What is the result of the expression?")
    score = 0
    right_answer = 0
    while score < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        x = opr.keys()
        x = list(x)
        operator = random.choice(x)
        question1 = (str(num1) + operator + str(num2))
        result = opr.get(operator)
        result = (result(num1, num2))
        print("question: " + str(question1))
        answer = prompt.integer("Your answer: ")
        if answer == result:
            correct()
            score += 1
            right_answer += 1
        elif answer != result:
            wrong()
            score += 1
        else:
            invalid()
        if right_answer == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
