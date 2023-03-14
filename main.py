# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import player_factory
import roster_creator
from positional_data import StandardPosition


def request_missing_players():
    players = player_factory.generate_full_cardinals()
    name_list = ''
    for player in players:
        name_list += f' | {player.name}'
    missing_player_raw_input = input(
        f'Which players will miss the game? \n'
        f'Player names: {name_list}\n'
        f'Enter names separated by commas: '
    )
    return player_factory.generate_available_players(missing_player_raw_input)


if __name__ == '__main__':
    print(f'Let\'s go, Cardinals!')
    players = request_missing_players()
    # roster = roster_creator.Roster(players, 6, False)
    roster = roster_creator.Roster(players, 6, is_shuffled=True)
    print(roster)
