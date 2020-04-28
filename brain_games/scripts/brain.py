import random
import prompt
from brain_games.cli import name

def welcome():
    return "Welcome to the brain Games!"

welcome()
print(f"Hello,{name}!")

def main(right_answer):
    
    
    def wrong():
        return print("You are wrong!")
    
    def invalid():
        return print("Invalid")

    def correct():
        return print("Correct!")
    times_played = 0
    user_right_answer = 0
    while times_played < 3:
        right_answer = right_answer1
        user_answer = prompt.integer("Your answer: ")
        if right_answer == user_answer:
            correct()
            user_right_answer += 1
            times_played += 1
        elif right_answer != user_answer:
            wrong()
            times_played += 1    
        else:
            invalid()
                
        if user_right_answer == 3:
            print(f"Congratulations, {name}!")
            
         
            
if __name__ == "__main__":
    main()
            


