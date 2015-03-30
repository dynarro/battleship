import unittest
import mock
from battleship import battlefield
from battleship import board


class TestBattleship(unittest.TestCase):
    def tearDown(self):
        board.reset_field()

    def test_generate_ship_location(self):
        pos1 = battlefield._generate_ship_position()
        pos2 = battlefield._generate_ship_position()
        self.assertNotEqual(pos1, pos2)

    def test_locate_ship(self):
        positions = [(0, 1),
                     (1, 2),
                     (2, 3),
                     (3, 4),
                     (4, 5),
                     (0, 2),
                     (1, 3),
                     (2, 4),
                     (3, 5),
                     (4, 0),
                     ]

        with mock.patch.object(battlefield,
                               '_generate_ship_position') as mock_method:

            mock_method.side_effect = positions
            battlefield.locate_ship()

            for pos in positions:
                self.assertTrue(battlefield.ship_in_pos(x=pos[0], y=pos[1]))

    def test_attack_ship(self):
        positions = [(0, 1),
                     (1, 2),
                     (2, 3),
                     (3, 4),
                     (4, 5),
                     (0, 2),
                     (1, 3),
                     (2, 4),
                     (3, 5),
                     (4, 0),
                     ]

        with mock.patch.object(battlefield,
                               '_generate_ship_position') as mock_method:

            mock_method.side_effect = positions
            battlefield.locate_ship()

            for pos in positions:
                self.assertTrue(battlefield.attack_ship(x=pos[0], y=pos[1]))

                # We made a second assertTrue bacause while the first
                # one verifies that the ship has been attacked, the
                # second one verifies that if we attack the ship that
                # has already been attacked,the ship is not there anymore.

                self.assertFalse(battlefield.attack_ship(x=pos[0], y=pos[1]))

    def test_guess_location(self):
        guess_positions = [0, 1]

        with mock.patch('__builtin__.raw_input') as raw_mock:
            raw_mock.side_effect = guess_positions

            with mock.patch.object(battlefield, 'wrong_guess') as wg_mock:
                wg_mock.side_effect = RuntimeError
                self.assertRaises(battlefield.guess_location)
