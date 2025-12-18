from typing import Dict, List, Tuple, Any
from utils.input_utils import ask_choice, ask_number

HOUSES = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
DEFAULT_HOUSES = {house: 0 for house in HOUSES}

def update_house_points(houses: Dict[str, int], house_name: str, points: int):

    if house_name not in houses :
        print(f"Warning: House '{house_name}' not found.")
        return
    houses[house_name] += points
    print(f"{house_name}: {points:+} points. New total: {houses[house_name]} points")


def display_winning_house(houses: Dict[str, int]) :

    if not houses:
        print("No houses data available.")
        return
    
    max_points = max(houses.values())
    winning_houses = [house for house, points in houses.items() if points == max_points]
    
    if len(winning_houses) == 1:
        print(f"\nThe winning house is {winning_houses[0]} with {max_points} points!")
    else:
        tied_houses = ", ".join(winning_houses)
        print(f"\nIt's a tie between {tied_houses} with {max_points} points each!")


def assign_house(character: Dict[str, Any], questions: List[Tuple[str, List[str], List[str]]]) :
    house_scores = {house: 0 for house in HOUSES}
    house_scores["Gryffindor"] += character.get("courage", 0) * 2
    house_scores["Slytherin"] += character.get("ambition", 0) * 2
    house_scores["Hufflepuff"] += character.get("loyalty", 0) * 2
    house_scores["Ravenclaw"] += character.get("intelligence", 0) * 2
    

    for i, (question, choices, house_weights) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        answer_index = ask_choice("Choose an answer:", choices) - 1
        chosen_house = house_weights[answer_index]
        house_scores[chosen_house] += 3  # Each answer is worth 3 points
    

    print("\nSummary of scores:")
    for house, score in sorted(house_scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{house}: {score} points")
    

    max_score = max(house_scores.values())
    winning_houses = [house for house, score in house_scores.items() if score == max_score]

    return winning_houses[0]

"""
def test_house_functions():
    print("=== Testing update_house_points ===")
    houses = DEFAULT_HOUSES.copy()
    update_house_points(houses, "Gryffindor", 20)
    update_house_points(houses, "Slytherin", 15)
    update_house_points(houses, "Hufflepuff", 10)
    update_house_points(houses, "Ravenclaw", 5)
    update_house_points(houses, "Gryffindor", -5)  # Remove points
    update_house_points(houses, "Hogwarts", 10)  # Non-existent house
    
    
    print("\n=== Testing display_winning_house ===")
    display_winning_house(houses)
    
    
    print("\n=== Testing assign_house ===")
    character = {
        "name": "Test Character",
        "courage": 5,
        "intelligence": 4,
        "loyalty": 3,
        "ambition": 2
    }
    
    questions = [
        ("You see a friend in danger. What do you do?",
         ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
         ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),
        
        ("Which trait describes you best?",
         ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
         ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),
        
        ("When faced with a difficult challenge, you...",
         ["Charge in without hesitation", "Look for the best strategy", "Rely on friends", "Analyze the problem"],
         ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])
    ]
    
    assigned_house = assign_house(character, questions)
    print(f"\nThe Sorting Hat has decided! You belong to... {assigned_house}!")

"""

   
