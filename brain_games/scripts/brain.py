import prompt


def welcome():
    return print("Welcome to the brain Games!")


def run(name=None, right_answer=None, question=None):

    print(f"Hello,{name}!")

    def wrong():
        return print("You are wrong!")

    def invalid():
        return print("Invalid")

    def correct():
        return print("Correct!")
    times_played = 0
    user_right_answer = 0
    num = 0
    while times_played < 3:
        print("Question:{}".format(question[num]))
        if type(right_answer[0]) == int:
            user_answer = prompt.integer("Your answer: ")
        else:
            user_answer = prompt.string("Your answer: ")
        if right_answer[num] == user_answer:
            correct()
            user_right_answer += 1
            times_played += 1
            num += 1
        elif right_answer[num] != user_answer:
            wrong()
            times_played += 1
            num += 1
        else:
            invalid()

        if user_right_answer == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    run(name=None, right_answer=None, question=None)
