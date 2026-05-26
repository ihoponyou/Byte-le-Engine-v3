from bytele.game.common.avatar import Avatar
from bytele.game.common.map.occupiable import Occupiable
from bytele.game.common.player import Player
from bytele.game.common.map.game_board import GameBoard
from bytele.game.common.enums import *
from bytele.game.constants import MOVE_TO_DIRECTION, MOVE_TO_DIRECTION_STR
from bytele.game.utils.vector import Vector
from bytele.game.controllers.controller import Controller


class MovementController(Controller):
    """
    `Movement Controller Notes:`

        The Movement Controller manages the movement actions the player tries to execute. Players can move up, down,
        left, and right. If the player tries to move into a space that's impassable, they don't move.

        For example, if the player attempts to move into an Occupiable Station (something the player can be on) that is
        occupied by a Wall object (something the player can't be on), the player doesn't move; that is, if the player
        tries to move into anything that can't be occupied by something, they won't move.
    """

    def __init__(self):
        super().__init__()


    def handle_actions(self, action: ActionType, client: Player, world: GameBoard):
        assert client.avatar is not None
        avatar = client.avatar

        direction = MOVE_TO_DIRECTION.get(action)
        if direction is None:
            return

        avatar.direction = MOVE_TO_DIRECTION_STR.get(action, "")
        destination: Vector = avatar.position + direction

        if not world.can_object_occupy(destination, avatar):
            return

        world.update_object_position(destination, avatar)
