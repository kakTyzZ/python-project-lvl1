#!/usr/bin/env python
import random
import prompt
from brain_games.cli import name


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
    print(f"Hello,{name}!")
    print('Answer "yes" if number even otherwise answer "no".')
    result = 0
    score = 0
    right_answer = 0
    while score < 3: 
        num = random_num()
        print("question: " + str(num))
        answer = prompt.string("Your answer: ")
        if num % 2 == 0 and answer == "yes" or answer == result:
            correct()
            score += 1
            right_answer += 1
        elif num % 2 == 1 and answer == "no":
            correct()
            score += 1  
            right_answer += 1
        elif num % 2 == 0 and answer == "no" or num % 2 == 1 and answer == "yes" or answer != result:
            wrong()
            score += 1
        else:
            invalid()
        if right_answer == 3:
            print(f"Congratulations, {name}!")


           
    
    



if __name__ == "__main__":
    main()


