from positional_data import StandardPosition


class Inning:
    def __init__(self, players):
        self.assigned_positions = fill_positions(players)
        self.players = players

    def __str__(self):
        printable = format_inning(self)
        return printable


def fill_positions(players):
    filled_positions = {}
    unassigned_players = players.copy()
    for position in StandardPosition:
        for i in range(0, len(unassigned_players)):
            if unassigned_players[i].field_group == position.value.field_group:
                filled_positions[position.value] = unassigned_players.pop(i)
                break
    return filled_positions

def format_inning(inning):
    printable = ""
    for position in inning.assigned_positions:
        printable += f"{position.name} :  {inning.assigned_positions[position]}\n"
    return printable

