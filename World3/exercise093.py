# Objective: Make a program that manager the efficiency of a soccer player.
# The program will read the player name and how many matches he played.
# Later, will read the amount of goals done in each match.
# At the end, all will storage in a dictionary, including the amount of goals done during the championship

# Programmer: Hugo Leça Ribeiro

player_date = dict()
goals = list()
name = str(input('Name: '))
matches = int(input('Matches: '))
for match in range(1, matches + 1):
    goals_match = int(input(f'How many goals in match number {match}? '))
    goals.append(goals_match)
player_date['Name'] = name
player_date['Goals'] = goals
player_date['Total'] = sum(goals)
print('-=' * 40)
for key, value in player_date.items():
    print(f'The field {key} have the value {value}.')
print('-=' * 40)
print(f'The soccer player {player_date.get("Name")} played {matches} matches. ')
for match in range(1, matches + 1):
    print(f'\t => In the match number {match}, did {goals[match - 1]} gols.')
print(f'Was a total of {player_date.get("Total")} goals.')
