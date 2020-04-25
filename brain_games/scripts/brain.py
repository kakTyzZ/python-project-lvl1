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
        
        

      








def main():
    
    def gcd_answer():
        right_answer = nod(num1, num2)
        return right_answer  
    def wrong():
        return print("You are wrong!")
    
    def invalid():
        return print("Invalid")

    def correct():
        return print("Correct!")
    times_played = 0
    user_right_answer = 0
    while times_played < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num = str(num1) + "," + str(num2)
        print(f"question: {num}")
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
            


