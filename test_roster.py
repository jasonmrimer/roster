import unittest

import player_factory
import roster_creator
from positional_data import StandardPosition


class MyTestCase(unittest.TestCase):
    def test_all_player_JSON(self):
        players = player_factory.generate()
        roster = roster_creator.create(
            players=players,
            inning_count=6
        )
        self.assertEqual(len(roster.innings), 6)


if __name__ == '__main__':
    unittest.main()
