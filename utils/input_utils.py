import json
from typing import List, Any, Union, Optional


def ask_text(message: str) -> str:
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        print("Error: Input cannot be empty. Please try again.")


def is_valid_number(s: str) -> bool:
    if not s:
        return False

    if s[0] == '-':
        s = s[1:]
        if not s:
            return False

    return all(c.isdigit() for c in s)


def ask_number(message: str, min_val: Optional[int] = None, max_val: Optional[int] = None) -> int:
    """
    Prompt the user to enter an integer within optional bounds.
    
    Args:
        message (str): The prompt message to display
        min_val (int, optional): Minimum allowed value (inclusive)
        max_val (int, optional): Maximum allowed value (inclusive)
        
    Returns:
        int: The validated number entered by the user
    """
    while True:
        user_input = input(message).strip()
        
        # Check if input is a valid number
        if not is_valid_number(user_input):
            print("Error: Please enter a valid integer.")
            continue
            
        num = int(user_input)

        if min_val is not None and num < min_val:
            if max_val is not None:
                print(f"Error: Please enter a number between {min_val} and {max_val}.")
            else:
                print(f"Error: Number must be at least {min_val}.")
            continue
            
        # Validate against max_val if provided
        if max_val is not None and num > max_val:
            if min_val is not None:
                print(f"Error: Please enter a number between {min_val} and {max_val}.")
            else:
                print(f"Error: Number must be at most {max_val}.")
            continue
            
        return num


def ask_choice(message: str, options: List[Any]) -> Any:
    """
    Display a numbered menu of options and get a valid choice from the user.
    
    Args:
        message (str): The prompt message to display
        options (List[Any]): List of options to choose from
        
    Returns:
        Any: The selected option from the list
    """
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


def load_file(file_path: str) -> Union[dict, list]:
    """
    Load and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        Union[dict, list]: The parsed JSON data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {file_path}: {str(e)}")


if __name__ == "__main__":
    # Test ask_text
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
