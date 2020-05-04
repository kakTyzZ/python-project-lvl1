#!/usr/bin/env python
import random
import operator
from brain_games.cli import name
from brain_games.scripts.brain import run, welcome


welcome()
name = name()


opr = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}
print("What is the result of the expression?")

right_answer = []
question = []

for i in range(3):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    x = opr.keys()
    x = list(x)
    operator = random.choice(x)
    question.append(str(num1) + operator + str(num2))
    result = opr.get(operator)
    right_answer.append(result(num1, num2))

run(right_answer=right_answer, question=question, name=name)


def main():
    pass


if __name__ == "__main__":
    main()
