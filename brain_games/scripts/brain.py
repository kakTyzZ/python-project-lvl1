import random
import prompt

def welcome():
    return "Welcome to the brain Games!"


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
      
def gcd_answer():
    RIGHT_ANSWER = nod(num1, num2)
    return RIGHT_ANSWER

def gcd_user_question():
    print(f"question: {num1},{num2}")




def main(*args):
    def wrong():
        return print("You are wrong!")
    
    def invalid():
        return print("Invalid")

    def correct():
        return print("Correct!")
    times_played = 0
    while times_played < 3:
        for i in args:
            right_answer = args[0]
            q = args[1]
        user_right_answer = 0
        right_answer = right_answer()
        print(q())
        USER_ANSWER = prompt.integer("Your answer: ")
        if right_answer > USER_ANSWER:
            correct()
            user_right_answer += 1
            times_played += 1
        elif right_answer < USER_ANSWER:
            wrong()
            times_played += 1    
        else:
            invalid()
                
        if user_right_answer == 3:
            print(f"Congratulations, {name}!")
            
if __name__ == "__main__":
    main()
            


