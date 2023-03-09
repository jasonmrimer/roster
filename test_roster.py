import unittest

import player_factory
import roster_creator


class MyTestCase(unittest.TestCase):
    def test_all_player_JSON(self):
        players = player_factory.generate(10)
        roster = roster_creator.create(
            players=players,
            inning_count=6)
        self.assertEqual(len(roster.innings), 6)
        for inning in roster.innings:
            unique_players = set(inning.players)
            self.assertEqual(len(unique_players), 10)


if __name__ == '__main__':
    unittest.main()
