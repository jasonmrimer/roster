from enum import Enum

from inning_creator import Inning


def move_select_players_to_top(select_players, players):
    for player in select_players:
        player_index = players.index(player)
        moving_player = players.pop(player_index)
        players.insert(0, moving_player)


def extract_benched_players(inning):
    benched_players = [assignment.player for assignment in inning.assignments if
        assignment.position.title == 'Bench']
    return benched_players


def create_innings(self, players, inning_count):
    innings = []
    for i in range(0, inning_count):
        inning = Inning(players)
        innings.append(inning)
        benched_players = extract_benched_players(inning)
        move_select_players_to_top(benched_players, players)
    return innings


def format(self):
    formatted_dict = dict()
    for player in self.players:
        formatted_dict[player.name] = ''
    for inning in self.innings:
        for assignment in inning.assignments:
            formatted_dict[assignment.player.name] += (f',{assignment.position.shorthand}')
    print(formatted_dict)
    return formatted_dict


class Roster():
    def __init__(self, players, inning_count):
        self.players = players
        self.innings = create_innings(self, self.players, inning_count)

    def __str__(self):
        formatted_dict = format(self)
        formatted_roster = f''
        for player in formatted_dict.keys():
            formatted_roster += f'\n{player},{formatted_dict[player]}'
        return formatted_roster