def init_character(last_name, first_name, attributes):

    return {
        "Last Name": str(last_name),
        "First Name": str(first_name),
        "Inventory": [],
        "Spells": [],
        "Attributes": dict(attributes),
        "Money": 100
    }


def display_character(character):
    print("Character profile:")
    print(f"Last name: {character['Last Name']}")
    print(f"First name: {character['First Name']}")
    print(f"Money: {character['Money']} galleons")

    print("Inventory:", ", ".join(character['Inventory']) if character['Inventory'] else "Empty")

    print("Spells:", ", ".join(character['Spells']) if character['Spells'] else "No spells learned")


    print("Attributes:")
    for attr, value in character['Attributes'].items():

        print(f"- {attr}: {value}")


def modify_money(character, amount):
    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer")
    character['Money'] += amount


def add_item(character, key, item):
    if key not in ['Inventory', 'Spells']:
        raise ValueError("Key must be either 'Inventory' or 'Spells'")
    character[key].append(str(item))