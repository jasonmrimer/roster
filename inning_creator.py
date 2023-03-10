from positional_data import StandardPosition, Position, FieldGroup


class Assignment:
    def __init__(self, position, player):
        self.position = position
        self.player = player


def bench_remaining(players, assignments):
    bench_position = Position(
        title="Bench", number=0, field_group=FieldGroup.BE
    )
    print(len(players))
    for player in players:
        assignments.append(
            Assignment(
                player=player,
                position=bench_position
            )
        )


class Inning:
    def __init__(self, players):
        self.assignments = assign_positions(players)
        bench_remaining(players, self.assignments)

    def __str__(self):
        printable = format_inning(self)
        return printable


def match_available_player(position, unassigned_players):
    for i in range(0, len(unassigned_players)):
        if unassigned_players[i].field_group == position.value.field_group:
            return unassigned_players.pop(i)


def assign_positions(players):
    assignments = []
    players
    for position in StandardPosition:
        available_player_match = match_available_player(
            position, players
        )
        if available_player_match:
            assignment = Assignment(
                position=position.value,
                player=available_player_match
            )
            assignments.append(assignment)

    return assignments


def format_inning(inning):
    printable = ""
    for position in inning.assignments:
        printable += f"{position.name} :  {inning.assignments[position]}\n"
    return printable
