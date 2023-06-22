from players import get_active_players
import pprint
import random

if __name__ == '__main__':
    players = list() # active player names
    player_list = list() # team list
    reroll_remaining = 1

    active_players = get_active_players()
    for p in active_players:
        players.append(p['full_name'])

    name = input("What is the player's name? ")
    
    while len(player_list) < 6:
        choices = random.choices(players, k=4)

        p = f'\nChoices: \n'
        for i, player in enumerate(choices):
            p += f'{i+1}: {player}\n'
        if reroll_remaining > 0:
            p += f'{len(choices)+1}: Reroll'

        print(p)

        chosen = int(input('\nWhich player? '))
        if chosen == len(choices)+1 and reroll_remaining > 0:
            print('Rerolling...\n')
            reroll_remaining -= 1
        else:
            player_list.append(choices[chosen-1])
            players.remove(choices[chosen-1])

        rep = f'\nTeam Name: {name} \n'
        for i, player in enumerate(player_list):
            rep += f'Player {i+1}: {player} \n'
        rep += '=============================='
        print(rep)