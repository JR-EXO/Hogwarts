import os
import sys
import json
from typing import Dict, List, Optional
from utils.input_utils import ask_text, ask_number, ask_choice, load_file
from universe.character import init_character, display_character, modify_money, add_item

def introduction():
    """Display the introductory text for Chapter 1."""

    print("\n" + "="*80)
    print("HARRY POTTER: THE HOGWARTS ADVENTURE")
    print("Chapter 1: The Boy Who Lived")

    print("="*80)
    print("\nWelcome to the magical world of Harry Potter!")
    print("You are about to embark on an extraordinary journey...")
    input("\nPress Enter to begin your adventure...")
    print("\n" + "-"*80)

def create_character() -> Dict:
    """Create and return the player's character."""
    print("\n" + "="*80)
    print("CHARACTER CREATION")
    print("="*80)

    # Get character's name
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")

    print("\nNow, distribute 20 points among these 4 attributes (1-10 each):")

    # Get attributes with validation to ensure total doesn't exceed 20
    while True:
        print("\nChoose your attributes (1-10 each, total must be ≤ 20):")
        courage = ask_number("Courage level (1-10): ", 1, 10)
        intelligence = ask_number("Intelligence level (1-10): ", 1, 10)
        loyalty = ask_number("Loyalty level (1-10): ", 1, 10)
        ambition = ask_number("Ambition level (1-10): ", 1, 10)

        total = courage + intelligence + loyalty + ambition
        if total <= 20:
            break
        print(f"\nError: Total points ({total}) exceed 20. Please redistribute your points.")

    # Create character with attributes
    attributes = {
        "Courage": courage,
        "Intelligence": intelligence,
        "Loyalty": loyalty,
        "Ambition": ambition
    }

    character = init_character(last_name, first_name, attributes)

    # Display character profile
    print("\n" + "-"*80)
    print("CHARACTER CREATED SUCCESSFULLY!")
    display_character(character)
    print("-"*80 + "\n")

    return character

def receive_letter() -> bool:
    """Handle the letter reception scene. Return True if player accepts, False otherwise."""
    print("\n" + "="*80)
    print("THE HOGWARTS LETTER")
    print("="*80)

    print("\nAn owl flies through the window, delivering a letter sealed with the Hogwarts crest...\n")
    print("""Dear Student,

We are pleased to inform you that you have been accepted to Hogwarts
School of Witchcraft and Wizardry! This is a rare honor, as you have been
selected from among thousands of young witches and wizards.

Term begins on September 1st. We await your response by owl post.

Yours sincerely,

Minerva McGonagall
Deputy Headmistress""")

    print("\n" + "-"*80)
    print("Do you accept this invitation and go to Hogwarts?")
    choice = ask_choice("Your choice: ", ["Yes, of course!", "No, I'd rather stay..."])

    if choice == 1:  # Yes
        print("\nExcellent! Your magical education is about to begin!")
        input("\nPress Enter to continue...")
        return True
    else:  # No
        print("\nYou tear up the letter, and your family cheers:")
        print("\"EXCELLENT! Finally, someone NORMAL in this house!\"")
        print("\nThe magical world will never know you existed... Game over.")
        input("\nPress Enter to exit...")
        sys.exit(0)

def meet_hagrid(character: Dict) -> None:
    """Handle the meeting with Hagrid."""
    print("\n" + "="*80)
    print("MEETING HAGRID")
    print("="*80)

    print("\nA loud BANG echoes through the house as someone knocks on the door.")
    print("A giant of a man with a wild, bushy beard enters the room.")
    print("\nHagrid: 'Blimey! You must be", character["First Name"], character["Last Name"] + "!")
    print("I'm Rubeus Hagrid, Keeper of Keys and Grounds at Hogwarts.'")
    print("I'm here to help you with your shoppin' on Diagon Alley.'")

    print("\n" + "-"*80)
    print("Do you want to follow Hagrid?")
    choice = ask_choice("Your choice: ", ["Yes", "No"])

    if choice == 1:  # Yes
        print("\nHagrid grins: 'Great! Follow me, we've got lots to do!'")
    else:  # No
        print("\nHagrid's smile fades for a moment, then he says:")
        print("'No time for second thoughts! Yer a wizard now, " + character["First Name"] + "!'")
        print("He gently but firmly takes your arm and leads you out the door.")

    input("\nPress Enter to continue to Diagon Alley...")

def buy_supplies(character: Dict) -> None:
    """Handle the shopping scene in Diagon Alley."""
    print("\n" + "="*80)
    print("DIAGON ALLEY")
    print("="*80)

    print("\nHagrid leads you through the Leaky Cauldron to a brick wall.")
    print("With a tap of his umbrella, the bricks rearrange themselves to reveal...")
    print("\nDIAGON ALLEY!")
    print("\nThe most magical shopping street in the wizarding world unfolds before you.")

    # Load inventory from JSON file
    try:
        inventory_data = load_file(os.path.join("data", "inventory.json"))
        items = inventory_data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nError: Could not load inventory data. Using default items.")
        items = [
            {"name": "Magic Wand", "price": 35, "required": True},
            {"name": "Wizard Robe", "price": 20, "required": True},
            {"name": "Potions Book", "price": 25, "required": True},
            {"name": "Tin Cauldron", "price": 15, "required": False},
            {"name": "Magic Quill", "price": 5, "required": False},
            {"name": "Enchanted Book", "price": 30, "required": False},
            {"name": "Copper Scale", "price": 10, "required": False},
            {"name": "Invisibility Cloak", "price": 100, "required": False}
        ]

    # Define pets separately
    pets = [
        {"name": "Owl", "price": 20},
        {"name": "Cat", "price": 15},
        {"name": "Rat", "price": 10},
        {"name": "Toad", "price": 5}
    ]

    # Shopping loop
    required_items = [item["name"] for item in items if item["required"]]
    purchased_items = []

    while required_items and character["Money"] > 0:
        print("\n" + "-"*80)
        print("Welcome to Diagon Alley!")
        print("Catalog of available items:")

        # Display available items
        for i, item in enumerate(items, 1):
            required = " (required)" if item["name"] in required_items else ""
            print(f"{i}. {item['name']} - {item['price']} Galleons{required}")

        print(f"\nYou have {character['Money']} Galleons.")
        if required_items:
            print(f"Remaining required items: {', '.join(required_items)}")

        # Get user's choice
        choice = ask_number("\nEnter the number of the item to buy (or 0 to finish shopping): ", 0, len(items))

        if choice == 0:  # Finish shopping
            break

        selected_item = items[choice - 1]

        # Check if already purchased
        if selected_item["name"] in purchased_items:
            print(f"You've already bought {selected_item['name']}!")
            continue


        if selected_item["price"] > character["Money"]:
            print("You don't have enough Galleons for that!")
            continue

        # Purchase item
        character["Money"] -= selected_item["price"]
        purchased_items.append(selected_item["name"])

        # Remove from required items if it was required
        if selected_item["name"] in required_items:
            required_items.remove(selected_item["name"])

        print(f"You bought: {selected_item['name']} (-{selected_item['price']} Galleons).")
        print(f"You have {character['Money']} Galleons left.")

        # Add to character's inventory
        add_item(character, "Inventory", selected_item["name"])

    # Check if all required items were purchased
    if required_items:
        print("\n" + "!"*80)
        print("Oh no! You didn't purchase all the required items!")
        print(f"You're missing: {', '.join(required_items)}")
        print("\nHagrid shakes his head: 'Yeh can't go to Hogwarts without all yer supplies!'")
        print("Game over!")
        input("\nPress Enter to exit...")
        sys.exit(0)

    # Pet selection
    print("\n" + "="*80)
    print("MAGICAL MENAGERIE")
    print("="*80)
    print("\nHagrid leads you to the Magical Menagerie to choose a pet.")
    print("\nIt's time to choose your Hogwarts pet!")
    print(f"You have {character['Money']} Galleons.")

    # Display available pets
    print("\nAvailable pets:")
    for i, pet in enumerate(pets, 1):
        print(f"{i}. {pet['name']} - {pet['price']} Galleons")

    # Get pet choice
    while True:
        try:
            print(f"\nYou have {character['Money']} Galleons left.")
            choice = ask_number("Which pet do you want? (enter number): ", 1, len(pets))
            selected_pet = pets[choice - 1]
#a
            if selected_pet["price"] > character["Money"]:
                print("You don't have enough Galleons for that pet!")
                continue

            # Purchase pet
            character["Money"] -= selected_pet["price"]
            print(f"\nYou chose: {selected_pet['name']} (-{selected_pet['price']} Galleons).")
            add_item(character, "Inventory", selected_pet["name"])
            break

        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

    # Final summary
    print("\n" + "="*80)
    print("PURCHASE SUMMARY")
    print("="*80)
    print("\nAll required items have been successfully purchased! Here is your final inventory:")
    display_character(character)
    print("\nHagrid claps his hands together: 'Brilliant! Now we're all set for Hogwarts!'")
    input("\nPress Enter to continue...")

def start_chapter_1() -> Dict:
    """Start Chapter 1 of the adventure."""
    # Initialize the chapter
    introduction()

    # Create character
    character = create_character()

    # Receive Hogwarts letter
    if not receive_letter():
        return None

    # Meet Hagrid
    meet_hagrid(character)

    # Go shopping in Diagon Alley
    buy_supplies(character)

    # End of chapter
    print("\n" + "="*80)
    print("END OF CHAPTER 1")
    print("="*80)
    print("\nYou've completed your shopping in Diagon Alley with Hagrid's help.")
    print("Now, it's time to board the Hogwarts Express at King's Cross Station!")
    print("\nYour magical education is about to begin...")
    input("\nPress Enter to continue to Chapter 2...")

    return character

if __name__ == "__main__":
    # This allows the chapter to be run directly for testing
    print("HARRY POTTER: THE HOGWARTS ADVENTURE")
    print("Chapter 1: The Boy Who Lived")
    print("-" * 80)

    player_character = start_chapter_1()

    if player_character:
        print("\nChapter 1 completed successfully!")
        print("Your character:")
        display_character(player_character)
    else:
        print("\nGame over. Better luck next time!")