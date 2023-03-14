import unittest

import player_factory
import roster_creator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.players = player_factory.generate_full_cardinals()
        self.roster = roster_creator.Roster(
            players=self.players.copy(), inning_count=6, is_shuffled=False
        )

    def test_all_innings_created(self):
        self.assertEqual(len(self.roster.innings), 6)

    def test_players_do_not_bench_consecutive_innings(self):
        for player in self.players:
            was_benched_previous = False
            for i in range(0, len(self.roster.innings)):
                inning = self.roster.innings[i]
                assignments_dict = {assignment.player: assignment.position
                    for assignment
                    in inning.assignments}
                assigned_position = assignments_dict[player]
                if was_benched_previous and assigned_position.title == 'Bench':
                    self.fail(
                        f'{player.name} sat consecutively in innings {i - 1} and {i}'
                    )
                elif assigned_position.title == 'Bench':
                    was_benched_previous = True
                else:
                    was_benched_previous = False

    def test_list_rearrange(self):
        select_players = [
            self.players[4],
            self.players[5],
            self.players[8],
            self.players[13],
        ]

        top_four_players = self.players[:4]
        self.assertEqual(14, len(self.players))
        for i in range(0, len(select_players)):
            self.assertFalse(select_players[i] in top_four_players)

        roster_creator.move_select_players_to_top(
            select_players,
            self.players
        )

        top_four_players = self.players[:4]
        self.assertEqual(14, len(self.players))
        for i in range(0, len(select_players)):
            self.assertTrue(select_players[i] in top_four_players)

    def test_all_players_max_bench_2_innings(self):
        players_over_max_bench = []
        for player in self.players:
            assignments = self.roster.assignments_by_player[player]
            bench_assignments = [
                position for position in assignments if
                position.shorthand == 'B']
            if len(bench_assignments) > 2:
                players_over_max_bench.append(player)

        self.assertEqual(
            len(players_over_max_bench),
            0,
            msg=f'{len(players_over_max_bench)} players sat more 2 innings'
        )


if __name__ == '__main__':
    unittest.main()
