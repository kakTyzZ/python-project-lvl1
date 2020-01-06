#!/usr/bin/env python
import random
import prompt

def greet():
    print("Welcome to the brain Games!")

def run():
    global name
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
greet()
run()


print('Answer "yes" if number even otherwise answer "no".')

def wrong():
    print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let\'s try again, {name} !")

def correct():
    print("Correct!")

def random_num():
    number = random.randint(1,20)
    return number
def invalid():
    print("You can type only 'yes' or 'no'!")    
    
for i in range(0,3):
    score = 0
    num = random_num()
    print("question: " + str(num))
    answer = prompt.string("Your answer: ")
    if num % 2 == 0 and answer == "yes":
        print(correct())
        score += 1
    elif num % 2 == 1 and answer == "no":
        print(correct())
        score += 1
    elif num % 2 == 0 and answer == "no" or num % 2 == 1 and answer == "yes":
        print(wrong())
    else:
        print(invalid())
if score == 3:
    print(f"Congratulations  {name}" )

if __name__ == "__main__":
    main()
