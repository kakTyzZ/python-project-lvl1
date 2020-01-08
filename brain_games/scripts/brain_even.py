#!/usr/bin/env python
import random
import prompt
from brain_games.cli import *
from brain import welcome


welcome()

name = name()

print(f"Hello,{name}!")

print('Answer "yes" if number even otherwise answer "no".')

def wrong():
    return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let\'s try again, {name} !")

def correct():
    return print("Correct!")
   

def random_num():
    number = random.randint(1,20)
    return number
def invalid():
    return print("You can type only 'yes' or 'no'!")    



def main():
    score = 0
    while score < 3:
        num = random_num()
        print("question: " + str(num))
        answer = prompt.string("Your answer: ")
        if num % 2 == 0 and answer == "yes":
            correct()
            score += 1
        elif num % 2 == 1 and answer == "no":
            correct()
            score += 1
        elif num % 2 == 0 and answer == "no" or num % 2 == 1 and answer == "yes":
            wrong()
            score += 1
        else:
            invalid()
            score += 1
        if score == 3:
            print(f"Congratulations, {name}!")
    
    



if __name__ == "__main__":
    main()


