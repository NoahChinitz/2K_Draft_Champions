import pandas as pd
import random
from termcolor import colored

BLUE = 'blue'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'


class Player(object):
    
    def __init__(self, name="name", rating="rating", team="team", position="position"):
        self.name = name
        self.rating = rating
        self.team = team
        self.position = position

    def __repr__(self):
        try:
            rep = f"\nName: {self.name}"
            rep += f"\nRating: {self.rating}"
            rep += f"\nTeam: {self.team}"
            rep += f"\nPosition: {self.position}\n"
        except Exception as e:
            print(e)
        return rep


class Team(object):

    def __init__(self, name):
        self.name = name
        self.g1 = None
        self.g2 = None
        self.f1 = None
        self.f2 = None
        self.c = None
        self.sub = None
        self.rerolls_remaining = 1
        self.rating = 0
    
    def __repr__(self):
        rep = f"\nTeam Name: {self.name}"
        if self.g1 is not None:
            rep += f"\nGuard #1: {self.g1}"
        if self.g2 is not None:
            rep += f"\nGuard #2: {self.g2}"
        if self.f1 is not None:
            rep += f"\nForward #1: {self.f1}"
        if self.f2 is not None:
            rep += f"\nForward #2: {self.f2}"
        if self.c is not None:
            rep += f"\nCenter: {self.c}"
        if self.sub is not None:
            rep += f"\nSub: {self.sub}"
        return rep


class Game(object):
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.player_list = list()
        self.guard_list = list()
        self.forward_list = list()
        self.center_list = list()
        self.create_player_lists()
    
    def create_player_lists(self):
        df = pd.read_csv('Player_Ratings.csv')
        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        for i, player in enumerate(df['Player']):
            p = Player(name=player, rating=df['Rating'][i], team=df['Team'][i], position=df['Position'][i])
            self.player_list.append(p)
        for player in self.player_list:
            if "G" in player.position:
                self.guard_list.append(player)
            if "F" in player.position:
                self.forward_list.append(player)
            if "C" in player.position:
                self.center_list.append(player)

    def get_choices(self, player_list, k):
        choices = random.choices(player_list, k=k)
        return choices

    def print_choices(self, choices):
        print(colored("Choices:", YELLOW))
        for i, player in enumerate(choices):
            print(f"{i+1}: {player}")

    def print_teams(self):
        print("="*50)
        print(colored(self.team1, RED))
        print("="*50)
        print(colored(self.team2, GREEN))
        print("="*50)

    def choose_guard_1(self):
        print("="*50)
        print(colored(f"{self.team1.name} pick your first guard", RED))
        choices = self.get_choices(self.guard_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team1.g1 = choices[chosen-1]
        self.guard_list.remove(self.team1.g1)
        self.player_list.remove(self.team1.g1)
        print("="*50)
        print(colored(f"{self.team2.name} pick your first guard", GREEN))
        choices = self.get_choices(self.guard_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team2.g1 = choices[chosen-1]
        self.guard_list.remove(self.team2.g1)
        self.player_list.remove(self.team2.g1)
        print("="*50)
        self.print_teams()

    def choose_guard_2(self):
        print("="*50)
        print(colored(f"{self.team1.name} pick your second guard", RED))
        choices = self.get_choices(self.guard_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team1.g2 = choices[chosen-1]
        self.guard_list.remove(self.team1.g2)
        self.player_list.remove(self.team1.g2)
        print("="*50)
        print(colored(f"{self.team2.name} pick your second guard", GREEN))
        choices = self.get_choices(self.guard_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team2.g2 = choices[chosen-1]
        self.guard_list.remove(self.team2.g2)
        self.player_list.remove(self.team2.g2)
        print("="*50)
        self.print_teams()

    def choose_forward_1(self):
        print("="*50)
        print(colored(f"{self.team1.name} pick your first forward", RED))
        choices = self.get_choices(self.forward_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team1.f1 = choices[chosen-1]
        self.forward_list.remove(self.team1.f1)
        self.player_list.remove(self.team1.f1)
        print("="*50)
        print(colored(f"{self.team2.name} pick your first forward", GREEN))
        choices = self.get_choices(self.forward_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team2.f1 = choices[chosen-1]
        self.forward_list.remove(self.team2.f1)
        self.player_list.remove(self.team2.f1)
        print("="*50)
        self.print_teams()
    
    def choose_forward_2(self):
        print("="*50)
        print(colored(f"{self.team1.name} pick your second forward", RED))
        choices = self.get_choices(self.forward_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team1.f2 = choices[chosen-1]
        self.forward_list.remove(self.team1.f2)
        self.player_list.remove(self.team1.f2)
        print("="*50)
        print(colored(f"{self.team2.name} pick your second forward", GREEN))
        choices = self.get_choices(self.forward_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team2.f2 = choices[chosen-1]
        self.forward_list.remove(self.team2.f2)
        self.player_list.remove(self.team2.f2)
        print("="*50)
        self.print_teams()

    def choose_center(self):
        print("="*50)
        print(colored(f"{self.team1.name} pick your center", RED))
        choices = self.get_choices(self.center_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team1.c = choices[chosen-1]
        self.center_list.remove(self.team1.c)
        self.player_list.remove(self.team1.c)
        print("="*50)
        print(colored(f"{self.team2.name} pick your center", GREEN))
        choices = self.get_choices(self.center_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team2.c = choices[chosen-1]
        self.center_list.remove(self.team2.c)
        self.player_list.remove(self.team2.c)
        print("="*50)
        self.print_teams()

    def choose_sub(self):
        print("="*50)
        print(colored(f"{self.team1.name} pick your sixth man", RED))
        choices = self.get_choices(self.player_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team1.sub = choices[chosen-1]
        self.player_list.remove(self.team1.sub)
        print("="*50)
        print(colored(f"{self.team2.name} pick your sixth man", GREEN))
        choices = self.get_choices(self.player_list, 4)
        self.print_choices(choices)
        chosen = int(input("\nWhich player? "))
        self.team2.sub = choices[chosen-1]
        self.player_list.remove(self.team2.sub)
        print("="*50)

    def get_ratings(self):
        team1_rating = (self.team1.g1.rating + self.team1.g2.rating + self.team1.f1.rating + self.team1.f2.rating + self.team1.c.rating + self.team1.sub.rating) / 6
        team2_rating = (self.team2.g1.rating + self.team2.g2.rating + self.team2.f1.rating + self.team2.f2.rating + self.team2.c.rating + self.team2.sub.rating) / 6
        return team1_rating, team2_rating

if __name__ == "__main__":
    # create first team
    t1 = input("What is the name of the first team? ")
    team1 = Team(t1)
    # create second team
    t2 = input("What is the name of the second team? ")
    team2 = Team(t2)
    print()
    # create game
    game = Game(team1, team2)
    # round 1
    game.choose_guard_1()
    # round 2
    game.choose_guard_2()
    # round 3
    game.choose_forward_1()
    # round 4
    game.choose_forward_2()
    # round 5
    game.choose_center()
    # round 6
    game.choose_sub()

    game.print_teams()
    team1_rating, team2_rating = game.get_ratings()
    print(colored(f"{team1.name} rating: {team1_rating}", YELLOW))
    print(colored(f"{team2.name} rating: {team2_rating}", YELLOW))