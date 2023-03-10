from enum import Enum

from inning_creator import Inning


def create(players, inning_count):
    innings = []
    for i in range(0, inning_count):
        innings.append(Inning(players))
    return Roster(innings)


class Roster():
    def __init__(self, innings):
        self.innings = innings
