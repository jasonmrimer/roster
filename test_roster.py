import unittest

import player_factory
import roster_creator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.players = player_factory.generate_full_cardinals()
        self.roster = roster_creator.Roster(
            players=self.players.copy(),
            inning_count=6
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
        selected_player_1 = self.players[4]
        selected_player_2 = self.players[5]
        selected_player_3 = self.players[8]
        selected_player_4 = self.players[13]
        select_players = [
            selected_player_1,
            selected_player_2,
            selected_player_3,
            selected_player_4,
        ]

        top_four_players = self.players[:4]
        self.assertEqual(14, len(self.players))
        self.assertFalse(selected_player_1 in top_four_players)
        self.assertFalse(selected_player_2 in top_four_players)
        self.assertFalse(selected_player_3 in top_four_players)
        self.assertFalse(selected_player_4 in top_four_players)

        roster_creator.move_select_players_to_top(
            select_players,
            self.players
        )

        top_four_players = self.players[:4]
        print(top_four_players)
        self.assertEqual(14, len(self.players))
        self.assertTrue(selected_player_1 in top_four_players)
        self.assertTrue(selected_player_2 in top_four_players)
        self.assertTrue(selected_player_3 in top_four_players)
        self.assertTrue(selected_player_4 in top_four_players)

if __name__ == '__main__':
    unittest.main()
