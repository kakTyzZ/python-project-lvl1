import random


print('Answer "yes" if number even otherwise answer "no".')

def wrong():
    print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let\'s try again, Bill!")

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
    else:
        print(invalid())
if score == 3:
    print("Congratulations" + name )
    
