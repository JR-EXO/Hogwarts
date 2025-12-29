import json
import random
from utils.input_utils import *


def load_teams():
    file_path = 'data/teams_quidditch.json'
    if not os.path.exists(file_path):
        print("Error: teams_quidditch.json not found!")
        return None

    with open(file_path, 'r') as f:
        return json.load(f)

def create_team(house, team_data, is_player=False, player=None):

    team = {
        'name': house,
        'score': 0,
        'players': team_data['players'].copy()
    }

    if is_player and player:
        seekers = [f"{player['name']} (Seeker)"]
        non_seekers = [p for p in team_data['players'] if player['name'] not in p]
        team['players'] = seekers + non_seekers
    
    return team

def attempt_goal(attacker, defender):
    if random.random() < 0.6:
        goalscorer = random.choice([p for p in attacker['players'] if "(Chaser)" in p])
        attacker['score'] += 10
        print(f"{goalscorer} scores for {attacker['name']}! (+10 points)")
    else:
        print(f"{defender['name']} blocks the attack!")

def golden_snitch_appears():
    return random.randint(1, 6) == 6

def catch_snitch(team1, team2):
    winner = random.choice([team1, team2])
    winner['score'] += 150
    print(f"\nThe Golden Snitch has been caught by {winner['name']}! (+150 points)")
    return winner

def display_score(team1, team2):
    print("\n" + "-"*30)
    print(f"SCORE: {team1['name']} {team1['score']} - {team2['score']} {team2['name']}")
    print("-"*30)

def display_teams(team1, team2):
    print("\n" + "="*50)
    print(f"QUIDDITCH MATCH: {team1['name'].upper()} vs {team2['name'].upper()}")
    print("="*50)
    
    for team in [team1, team2]:
        print(f"\n{team['name']} Team:")
        for player in team['players']:
            print(f"- {player}")

def play_quidditch(character, houses):
    teams_data = load_teams()
    if not teams_data:
        return
    
    player_house = character['house']
    opponent_house = random.choice([h for h in teams_data.keys() if h != player_house])
    
    player_team = create_team(player_house, teams_data[player_house], True, character)
    opponent_team = create_team(opponent_house, teams_data[opponent_house])
    
    display_teams(player_team, opponent_team)
    print(f"\nYou are playing as {character['name']}, Seeker for {player_house}!")
    input_continue("\nPress Enter to start the match...")
    
    turn = 1
    game_over = False
    
    while turn <= 20 and not game_over:
        print(f"\n━ Turn {turn} ━")
        
        print(f"\n{player_team['name']} attacks:")
        attempt_goal(player_team, opponent_team)
        
        print(f"\n{opponent_team['name']} attacks:")
        attempt_goal(opponent_team, player_team)
        
        if golden_snitch_appears():
            winner = catch_snitch(player_team, opponent_team)
            game_over = True
        
        if not game_over:
            display_score(player_team, opponent_team)
            input_continue("\nPress Enter to continue...")
            turn += 1
    
    print("\n" + "="*50)
    print("MATCH ENDED!")
    print(f"Final Score: {player_team['name']} {player_team['score']} - {opponent_team['score']} {opponent_team['name']}")
    
    if player_team['score'] > opponent_team['score']:
        winning_house = player_house
        print(f"\n{player_house} wins the match!")
    elif player_team['score'] < opponent_team['score']:
        winning_house = opponent_house
        print(f"\n{opponent_house} wins the match!")
    else:
        print("\nIt's a draw!")
        return
    
    houses[winning_house] = houses.get(winning_house, 0) + 500
    print(f"\n{winning_house} earns 500 points for the House Cup!")

def start_chapter_4(character, houses):
    print("\n" + "="*50)
    print("CHAPTER 4: THE QUIDDITCH FINAL")
    print("="*50)
    
    print("\nThe Quidditch final is here! The stands are packed with cheering students.")
    print("The air is electric with excitement as you prepare to represent your house!")
    
    input_continue("\nPress Enter to begin the match...")
    
    play_quidditch(character, houses)
    
    print("\n" + "="*50)
    print("END OF CHAPTER 4")
    print("="*50)
    
    print("\nCurrent House Points:")
    house_list = [(house, points) for house, points in houses.items()]
    
    n = len(house_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if house_list[j][1] < house_list[j + 1][1]:
                house_list[j], house_list[j + 1] = house_list[j + 1], house_list[j]
    
    for house, points in house_list:
        print(f"{house}: {points} points")
    
    input_continue("\nPress Enter to continue your adventure...")

"""
if __name__ == "__main__":
    test_character = {
        'name': 'Harry Potter',
        'house': 'Gryffindor'
    }
    
    test_houses = {
        'Gryffindor': 100,
        'Hufflepuff': 80,
        'Ravenclaw': 90,
        'Slytherin': 120
    }
    
    start_chapter_4(test_character, test_houses)
""""