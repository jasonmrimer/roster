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
    def setUp(self) -> None:
        self.players = player_factory.generate_full_cardinals()
        self.inning = Inning(self.players.copy())
        self.assignments = self.inning.assignments

    def test_all_positions_covered_on_inning_creation(self):
        assignments_dict = {assignment.position: assignment.player
            for assignment
            in self.assignments}

        for position in StandardPosition:
            self.assertTrue(position.value in assignments_dict.keys())

            player_at_position = assignments_dict[position.value]
            self.assertIsNotNone(player_at_position)

    def test_all_players_assigned_to_position_and_bench(self):
        assigned_players = set(
            [assignment.player for assignment in self.assignments]
        )
        self.assertEqual(len(self.players), len(assigned_players))

        benched_players = collect_benched_players(self.inning)
        self.assertEqual(4, len(benched_players))

    def test_players_assign_to_fielder_group(self):
        non_bench_assignments = [
            assignment for assignment in self.assignments
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
