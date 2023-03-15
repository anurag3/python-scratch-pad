import unittest
import pytest
from ..robot import Robot


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(x=0, y=0)

    def test_initialized_state(self):
        curr_x, curr_y = self.robot.get_position()
        expected_x, expected_y = 0, 0
        self.assertEqual(curr_x, expected_x)
        self.assertEqual(curr_y, expected_y)

    def test_set_position(self):
        x = 2
        y = 3
        self.robot.set_position(x, y)
        curr_x, curr_y = self.robot.get_position()
        self.assertEqual(curr_x, x)
        self.assertEqual(curr_y, y)

    def test_empyt_moveset(self):
        move = ""
        self.robot.move(move)
        curr_x, curr_y = self.robot.get_position()
        self.assertEqual(curr_x, 0)
        self.assertEqual(curr_y, 0)

    def test_single_char_moveset(self):
        move = "U"
        self.robot.move(move)
        curr_x, curr_y = self.robot.get_position()
        self.assertEqual(curr_x, 0)
        self.assertEqual(curr_y, 1)

    def test_happy_path_moveset(self):
        move = "UUUL"
        self.robot.move(move)
        curr_x, curr_y = self.robot.get_position()
        self.assertEqual(curr_x, -1)
        self.assertEqual(curr_y, 3)

    def test_error_path_moveset(self):
        move = "AUUL"
        with pytest.raises(ValueError):
            self.robot.move(move)
