import json
from typing import List, Any, Union, Optional


def ask_text(message: str):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        print("Error: Input cannot be empty. Please try again.")


def is_valid_number(s: str) :
    if not s:
        return False

    if s[0] == '-':
        s = s[1:]
        if not s:
            return False

    return all(c.isdigit() for c in s)


def ask_number(message, min_val=None, max_val=None):
    user_input = input(message)
    valid_digits = "0123456789"
    is_valid = True

    if len(user_input) == 0 :
        is_valid = False

    is_negative = False
    if user_input[0] == '-':
        is_negative = True
        user_input = user_input[1:]

    for v in user_input:
        if v not in valid_digits:
            is_valid = False

    if not is_valid:
        print("Not valid. Please enter a valid integer.")
        return ask_number(message, min_val, max_val)

    number = 0

    for i in user_input:
        unit = ord(i) - ord('0')
        number = number * 10 + unit

    if is_negative:
        number = -number
    if min_val is not None and number < min_val or max_val is not None and number > max_val:
        print(f"Please enter a number between {min_val} and {max_val}.")
        return ask_number(message, min_val, max_val)

    return number


def ask_choice(message: str, options: List[Any]) :
    if not options:
        raise ValueError("No options provided")

    print(message)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = ask_number("Your choice: ", 1, len(options))
            return options[choice - 1]
        except (ValueError, IndexError):
            print(f"Please enter a number between 1 and {len(options)}")


def load_file(file_path: str):


    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {file_path}: {str(e)}")


if __name__ == "__main__":
    name = ask_text("Enter your character's name: ")
    print(f"Welcome, {name}!")

    age = ask_number("Enter your age: ", 1, 150)
    print(f"You are {age} years old.")

    choice = ask_choice("Choose your house:", ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"])
    print(f"You chose: {choice}")
    try:
        data = load_file("test.json")
        print("File loaded successfully:", data)
    except Exception as e:
        print(f"Error loading file: {e}")
