from utils.input_utils import *

def display_main_menu():
    print("\n=== HOGWARTS ADVENTURE ===\n")
    print("1. Start Chapter 1 - Arrival in the magical world")
    print("2. Exit the game\n")

def launch_menu_choice():
    houses = [{"name": "Gryffindor", "points": 0},
        {"name": "Hufflepuff", "points": 0},
        {"name": "Ravenclaw", "points": 0},
        {"name": "Slytherin", "points": 0}
        ]
    display_main_menu()
    choice = ask_text("Enter your choice (1-2): ")
    
    if choice == "1":
        print("\n=== Chapter 1: Arrival in the Magical World ===\n")
        from chapters.chapter_1 import start_chapter_1
        player_name = start_chapter_1()

        print("\n=== Chapter 2: Journey to Hogwarts ===\n")
        from chapters.chapter_2 import start_chapter_2
        house = start_chapter_2(player_name)

        print(f"\n=== Chapter 3: Magic and Spells at {house} ===\n")
        from chapters.chapter_3 import start_chapter_3
        start_chapter_3(player_name,houses)

        print("\n=== Chapter 4: The Quidditch Challenge ===\n")
        from chapters.chapter_4 import start_chapter_4
        start_chapter_4(player_name, houses)



    elif choice == "2":
        print("\nThank you for playing Hogwarts Adventure!")
        print("The game will now close. Goodbye!")

    else:
        print("\nInvalid choice. Please enter 1 or 2.")
"""
if __name__ == "__main__":
    launch_menu_choice()
"""