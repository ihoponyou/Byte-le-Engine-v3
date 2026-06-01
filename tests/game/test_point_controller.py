import unittest

from bytele.game.common.avatar import Avatar
from bytele.game.common.map.game_board import GameBoard
from bytele.game.controllers.point_controller import PointController
from bytele.game.utils.vector import Vector


class TestPointController(unittest.TestCase):
    def setUp(self) -> None:
        self.point_controller = PointController()
        self.avatar: Avatar = Avatar()
        self.game_board: GameBoard = GameBoard(0, map_size=Vector(2, 2), locations={
            Vector(0, 0): [self.avatar],
        })
        self.game_board.generate_map()

    def test_points_given_every_turn(self):
        self.assertEqual(self.avatar.score, 0)
        turns = 13
        for _ in range(turns):
            self.point_controller.handle_actions(self.avatar, self.game_board)
        self.assertGreater(self.avatar.score, 0)
        self.assertEqual(self.avatar.score, self.point_controller.base_points_per_turn * turns)

