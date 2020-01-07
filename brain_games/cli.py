import prompt


def greet():
    name = prompt.string('May i have your name? ')
    return f"Hello, {name}!"
    
    


if __name__ == "__main__":
    main()
