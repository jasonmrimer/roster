from unittest import TestCase

import player_factory
from positional_data import FieldGroup


class TestPlayer(TestCase):
    def test_input_formatter(self):
        raw_input = 'chad,azriel, Hoku,   KOA'

        formatted_output = player_factory.format_raw_input(raw_input)

        self.assertEqual(
            ['chad', 'azriel', 'hoku', 'koa'],
            formatted_output
        )

    def test_players_from_raw_input(self):
        raw_input = 'chad,azriel, Hoku,   KOA'

        players = player_factory.generate_available_players(raw_input)

        self.assertEqual(
            players,
            [
                player_factory.Player('Carter', FieldGroup.IF),
                player_factory.Player('Eli', FieldGroup.OF),
                player_factory.Player('Elijah', FieldGroup.IF),
                player_factory.Player('Grayson', FieldGroup.IF),
                player_factory.Player('Julian', FieldGroup.OF),
                player_factory.Player('Kamuela', FieldGroup.IF),
                player_factory.Player('Mason', FieldGroup.IF),
                player_factory.Player('Peyton', FieldGroup.IF),
                player_factory.Player('Rhaeden', FieldGroup.IF),
                player_factory.Player('Roman', FieldGroup.OF),
            ]
        )
