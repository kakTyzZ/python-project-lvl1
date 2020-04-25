#!/usr/bin/env python
import random
from brain_games.cli import name
import prompt
from brain_games.scripts.brain import main,gcd_user_question,gcd_answer,nod

print("Find the greatest common divisor of given numbers.")





main(gcd_answer,gcd_user_question)


if __name__ == "__main__":
    main()


