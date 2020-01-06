import prompt


def run():
    global name
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
