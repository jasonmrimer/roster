# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import player_factory
import roster_creator
from positional_data import StandardPosition


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Let\'s go, Cardinals!')
    players = player_factory.generate_full_cardinals()
    roster = roster_creator.Roster(players, 6)
    print(roster)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
