import json
import os
from typing import Dict, List, Tuple

def meet_friends(character: Dict[str, any]):
    print("\nYou board the Hogwarts Express. The train slowly departs northward...")

    print("\nA red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    
    choice = input("Your choice (1-2): ")
    if choice == "1":
        character["loyalty"] += 1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else:
        character["ambition"] += 1
        print("Ron shrugs: — Suit yourself. See you around, I guess.")
    

    print("\nA girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")
    
    choice = input("Your choice (1-2): ")
    if choice == "1":
        character["intelligence"] += 1
        print("Hermione smiles: — Oh, that's rare! You must be very clever!")
    else:
        character["courage"] += 1
        print("Hermione raises an eyebrow: — Well, I suppose adventures can be educational too.")

    print("\nA blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")
    
    choice = input("Your choice (1-3): ")
    if choice == "1":
        character["ambition"] += 1
        print("Draco smirks: — Wise choice. We'll see if you're worthy.")
    elif choice == "2":
        character["loyalty"] += 1
        print("Draco frowns: — You'll regret that!")
    else:
        character["courage"] += 1
        print("Draco's eyes narrow: — Watch your back.")
    
    print("\nThe train continues its journey. Hogwarts Castle appears on the horizon...")
    print("\nYour choices already say a lot about your personality!")
    print(f"Your updated attributes: {character}")

def welcome_message():
    print("\n" + "="*50)
    print("As you enter the Great Hall for the first time, the ceiling shows a starry sky.")
    print("Professor Dumbledore stands and raises his hands for silence.")
    print("\n'Welcome! Welcome to a new year at Hogwarts! I have a few start-of-term notices...'")
    print("After his speech, the Sorting Hat is brought out.")
    input("\nPress Enter to continue...")

def sorting_ceremony(character: Dict[str, any]):
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]
    
    house_scores = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}
    
    print("\nThe Sorting Hat is placed on your head...")
    print("Hmm... difficult. Very difficult. Let's see...")
    
    for i, (question, options, houses) in enumerate(questions, 1):
        print(f"\n{question}")
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")

        choice = input("\nYour choice (1-4): ")
        while not (choice.isdigit() and 1 <= int(choice) <= 4):
            print("Please enter a number between 1 and 4.")
            choice = input("\nYour choice (1-4): ")
        selected_house = houses[int(choice)-1]
        house_scores[selected_house] += 10 - (i-1)
        
        if i < len(questions):
            print("\n'Interesting... very interesting...' the Hat murmurs.")

    house_scores["Gryffindor"] += character.get("courage", 0)
    house_scores["Slytherin"] += character.get("ambition", 0)
    house_scores["Hufflepuff"] += character.get("loyalty", 0)
    house_scores["Ravenclaw"] += character.get("intelligence", 0)


    sorted_houses = sorted(house_scores.items(), key=lambda x: x[1], reverse=True)
    character["house"] = sorted_houses[0][0]
    
    print("\nSummary of scores:")
    for house, score in sorted_houses:
        print(f"{house}: {score} points")
    
    print(f"\nThe Sorting Hat exclaims: {character['house']}!!!")
    print(f"You join the {character['house']} students to loud cheers!")

def enter_common_room(character: Dict[str, any]):
    house = character.get("house", "")
    house_info = {}
    
    houses_path = os.path.join("universe", "houses.json")
    if os.path.exists(houses_path) and os.path.isfile(houses_path):
        with open(houses_path, 'r') as f:
            houses_data = json.load(f)
            house_info = next((h for h in houses_data if h["name"] == house), {})
    else:
        print("Error: Could not load house information.")
        return
    
    print("\nYou follow the prefects through the castle corridors...")
    
    if house == "Gryffindor":
        print("🦁 You enter a cozy common room with plush armchairs and a roaring fire.")
    elif house == "Slytherin":
        print("🐍 You discover a vaulted common room, illuminated by the green glow of the lake.")
    elif house == "Hufflepuff":
        print("🦡 You step into a warm, round room with honey-colored wood and lots of plants.")
    else:  # Ravenclaw
        print("🦅 You enter a spacious, airy room with a domed ceiling painted with stars.")
    
    print(f"✨ {house_info.get('welcome_message', 'Welcome to your new home!')}")
    print(f"Your house colors: {house_info.get('colors', 'unknown')}")

def start_chapter_2(character: Dict[str, any]):

    print("\n" + "="*50)
    print("CHAPTER 2: THE JOURNEY TO HOGWARTS")
    print("="*50)

    meet_friends(character)

    welcome_message()

    sorting_ceremony(character)

    enter_common_room(character)

    print("\n" + "="*50)
    print("YOUR CHARACTER SUMMARY:")
    print("-"*50)
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

    print("\n" + "="*50)
    print("CHAPTER 2 COMPLETE!")
    print("Your journey at Hogwarts is just beginning...")
    print("Classes start tomorrow - be ready for new adventures!")
    print("="*50 + "\n")


