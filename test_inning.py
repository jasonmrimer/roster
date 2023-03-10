import unittest

import player_factory
from inning_creator import Inning
from positional_data import StandardPosition


class MyTestCase(unittest.TestCase):
    def test_all_positions_covered_on_inning_creation(self):
        players = player_factory.generate()
        inning = Inning(players)
        for position in StandardPosition:
            full_position = position.value
            self.assertTrue(full_position in inning.assigned_positions.keys())
            player_at_position = inning.assigned_positions[full_position]
            self.assertIsNotNone(player_at_position)
            self.assertEqual(
                len(set(inning.assigned_positions.values())),
                len(StandardPosition)
            )

    def test_all_players_assigned_to_position_and_bench(self):
        players = player_factory.generate()
        assignments = Inning(players).assigned_positions
        standard_positions = list(map(lambda pos: pos.value, StandardPosition))

        unassigned_players = [player for player in players if not self.player_has_assignment(
            player,
            assignments
        )]
        self.assertEqual(len(unassigned_players), 0)

    def test_players_assign_to_fielder_group(self):
        players = player_factory.generate()
        inning = Inning(players)
        for assigned_position in inning.assigned_positions:
            player = inning.assigned_positions[assigned_position]
            self.assertEqual(
                player.field_group,
                assigned_position.field_group
            )

    def find_by_player(self, assignments, search_player):
        player_list = []
        player_list = [position for position, player in assignments.items() if player == search_player]
        if len(player_list) > 0:
            return player_list.pop()
        return

    def player_has_assignment(self, player, assignments):
        assignment = self.find_by_player(assignments, player)
        return assignment != None


if __name__ == '__main__':
    unittest.main()
