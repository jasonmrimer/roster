import unittest
import player_factory
from inning_creator import Inning
from positional_data import StandardPosition


def collect_benched_players(inning):
    bench_assignments = [
        assignment for assignment in inning.assignments
        if assignment.position.title == "Bench"
    ]
    return bench_assignments


def find_by_player(assignments, search_player):
    player_list = [
        position for position, player in assignments.items()
        if player == search_player
    ]
    if len(player_list) > 0:
        return player_list.pop()


def player_has_assignment(player, assignments):
    assignment = find_by_player(assignments, player)
    return assignment is not None


class MyTestCase(unittest.TestCase):
    def test_all_positions_covered_on_inning_creation(self):
        players = player_factory.generate_full_cardinals()
        inning = Inning(players)
        assignments = {assg.position: assg.player for assg in
            inning.assignments}

        for position in StandardPosition:
            self.assertTrue(position.value in assignments.keys())

            player_at_position = assignments[position.value]
            self.assertIsNotNone(player_at_position)

    def test_all_players_assigned_to_position_and_bench(self):
        players = player_factory.generate_full_cardinals()
        inning = Inning(players.copy())
        assignments = inning.assignments

        assigned_players = set(
            [assignment.player for assignment in assignments]
        )
        self.assertEqual(len(players), len(assigned_players))

        benched_players = collect_benched_players(inning)
        self.assertEqual(4, len(benched_players))

    def test_players_assign_to_fielder_group(self):
        players = player_factory.generate_full_cardinals()
        inning = Inning(players)
        non_bench_assignments = [
            assignment for assignment in inning.assignments
            if assignment.position.title != 'Bench'
        ]

        for assignment in non_bench_assignments:
            player = assignment.player
            self.assertEqual(
                player.field_group,
                assignment.position.field_group
            )


import unittest

if __name__ == '__main__':
    unittest.main()
