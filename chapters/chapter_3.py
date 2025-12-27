import json
import random
import os
from typing import Dict, List, Any

def load_json_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def input_continue(prompt: str = "Press Enter to continue..."):
    input(prompt)

def learn_spells(character: Dict[str, Any], file_path: str = "../data/spells.json"):
    abs_path = os.path.join(os.path.dirname(__file__), file_path)
    all_spells = load_json_file(abs_path)
    offensive_spells = [s for s in all_spells if s['type'].lower() == 'offensive']
    defensive_spells = [s for s in all_spells if s['type'].lower() == 'defensive']
    utility_spells = [s for s in all_spells if s['type'].lower() == 'utility']
    if 'spells' not in character:
        character['spells'] = []
    
    print("\nYou begin your magic lessons at Hogwarts...")
    if offensive_spells:
        spell = random.choice(offensive_spells)
        character['spells'].append(spell)
        print(f"\nYou have just learned the spell: {spell['name']} ({spell['type']})")
        input_continue()

    if defensive_spells:
        spell = random.choice(defensive_spells)
        character['spells'].append(spell)
        print(f"\nYou have just learned the spell: {spell['name']} ({spell['type']})")
        input_continue()

    for _ in range(3):
        if utility_spells:
            spell = random.choice(utility_spells)
            while spell in character['spells'] and len(utility_spells) > len([s for s in character['spells'] if s['type'].lower() == 'utility']):
                spell = random.choice(utility_spells)
            
            character['spells'].append(spell)
            print(f"\nYou have just learned the spell: {spell['name']} ({spell['type']})")
            input_continue()

    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for spell in character['spells']:
        print(f"\n-  {spell['name']} ({spell['type']}): {spell['description']}")

def magic_quiz(character: Dict[str, Any], file_path: str = "../data/magic_quiz.json") -> int:
    abs_path = os.path.join(os.path.dirname(__file__), file_path)

    all_questions = load_json_file(abs_path)

    selected_questions = []
    while len(selected_questions) < 4 and all_questions:
        question = random.choice(all_questions)
        if question not in selected_questions:
            selected_questions.append(question)
    
    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.\n")
    
    score = 0

    for i, qa in enumerate(selected_questions, 1):
        print(f"{i}. {qa['question']}")
        answer = input(">  ").strip()
        
        if answer.lower() == qa['answer'].lower():
            score += 25
            print("Correct answer! +25 points for your house.")
        else:
            print(f"Wrong answer. The correct answer was: {qa['answer']}")
    
    print(f"\nScore obtained: {score} points")
    

    if 'score' not in character:
        character['score'] = 0
    character['score'] += score
    
    return score

def update_house_points(houses: List[Dict[str, Any]], house_name: str, points: int):

    for house in houses:
        if house['name'].lower() == house_name.lower():
            house['points'] = house.get('points', 0) + points
            break

def get_leading_house(houses: List[Dict[str, Any]]) -> str:

    if not houses:
        return "No houses available"

    leading_house = max(houses, key=lambda h: h.get('points', 0))
    return leading_house['name']

def display_character_info(character: Dict[str, Any]):

    print("\n=== Character Information ===")
    print(f"Name: {character.get('name', 'Unknown')}")
    print(f"House: {character.get('house', 'Not assigned')}")
    print(f"Score: {character.get('score', 0)} points")
    
    if 'spells' in character and character['spells']:
        print("\nSpells known:")
        for spell in character['spells']:
            print(f"- {spell['name']} ({spell['type']}): {spell['description']}")
    
    print("=" * 30)

def start_chapter_3(character: Dict[str, Any], houses: List[Dict[str, Any]]):
    print("\n" + "=" * 50)
    print("CHAPTER 3: CLASSES AND DISCOVERING HOGWARTS")
    print("=" * 50)

    learn_spells(character)

    input_continue("\nPress Enter to start the magic quiz...")
    score = magic_quiz(character)

    if 'house' in character:
        update_house_points(houses, character['house'], score)
        print(f"\n{character['house']} has earned {score} points!")

    leading_house = get_leading_house(houses)
    print(f"\nCurrent house standings:")
    for house in sorted(houses, key=lambda h: h.get('points', 0), reverse=True):
        print(f"- {house['name']}: {house.get('points', 0)} points")
    print(f"\n{leading_house} is in the lead!")

    input_continue("\nPress Enter to view your character information...")
    display_character_info(character)
    
    print("\nEnd of Chapter 3. Well done on completing your first magic lessons at Hogwarts!")

"""
if __name__ == "__main__":
    # Create a test character
    test_character = {
        "name": "Test Student",
        "house": "Gryffindor",
        "score": 0
    }
    

    test_houses = [
        {"name": "Gryffindor", "points": 0},
        {"name": "Hufflepuff", "points": 0},
        {"name": "Ravenclaw", "points": 0},
        {"name": "Slytherin", "points": 0}
    ]
    

    start_chapter_3(test_character, test_houses)
"""