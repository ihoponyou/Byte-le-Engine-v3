import unittest

from bytele.game.common.map.game_board import GameBoard
from bytele.game.controllers.movement_controller import MovementController
from bytele.game.common.stations.station import Station
from bytele.game.common.stations.occupiable_station import OccupiableStation
from bytele.game.common.map.wall import Wall
from bytele.game.utils.vector import Vector
from bytele.game.common.player import Player
from bytele.game.common.action import ActionType
from bytele.game.common.avatar import Avatar
from bytele.game.common.game_object import GameObject
import bytele.game.test_suite.utils

class TestMovementControllerIfWall(unittest.TestCase):
    """
    `Test Movement Controller with Stations Notes:`

        This class tests the different methods in the Movement Controller and that the Avatar can't pass Wall objects.
    """

    def setUp(self) -> None:
        self.movement_controller = MovementController()
        self.avatar = Avatar(Vector(2, 2), 1)

        self.locations: dict[Vector: list[GameObject]] = {
            Vector(2, 2): [self.avatar]
        }

        self.game_board = GameBoard(0, Vector(4, 4), self.locations, True)
        self.station = Station()
        self.occupiable_station = OccupiableStation()
        self.wall = Wall()
        self.client = Player(None, None, [], self.avatar)
        self.game_board.generate_map()
        self.utils = game.test_suite.utils

    def test_move_up(self):
        self.movement_controller.handle_actions(ActionType.MOVE_UP, self.client, self.game_board)
        self.assertEqual(str(self.client.avatar.position), str(Vector(2, 1)))

    def test_move_up_fail(self):
        self.movement_controller.handle_actions(ActionType.MOVE_UP, self.client, self.game_board)
        self.movement_controller.handle_actions(ActionType.MOVE_UP, self.client, self.game_board)
        self.assertEqual(str(self.client.avatar.position), str(Vector(2, 1)))

    def test_move_down(self):
        self.movement_controller.handle_actions(ActionType.MOVE_UP, self.client, self.game_board)
        self.movement_controller.handle_actions(ActionType.MOVE_DOWN, self.client, self.game_board)
        self.assertEqual(str(self.client.avatar.position), str(Vector(2, 2)))

    def test_move_down_fail(self):
        self.movement_controller.handle_actions(ActionType.MOVE_DOWN, self.client, self.game_board)
        self.assertEqual(self.client.avatar.position, Vector(2, 2))

    def test_move_left(self):
        self.movement_controller.handle_actions(ActionType.MOVE_LEFT, self.client, self.game_board)
        self.assertEqual(self.client.avatar.position, Vector(1, 2))

    def test_move_left_fail(self):
        self.movement_controller.handle_actions(ActionType.MOVE_LEFT, self.client, self.game_board)
        self.movement_controller.handle_actions(ActionType.MOVE_LEFT, self.client, self.game_board)
        self.assertEqual(self.client.avatar.position, Vector(1, 2))

    def test_move_right(self):
        self.movement_controller.handle_actions(ActionType.MOVE_LEFT, self.client, self.game_board)
        self.movement_controller.handle_actions(ActionType.MOVE_RIGHT, self.client, self.game_board)
        self.assertEqual(self.client.avatar.position, Vector(2, 2))

    def test_move_right_fail(self):
        self.movement_controller.handle_actions(ActionType.MOVE_RIGHT, self.client, self.game_board)
        self.assertEqual(self.client.avatar.position, Vector(2, 2))
