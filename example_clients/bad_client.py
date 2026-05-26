from bytele.game.client.user_client import UserClient
from bytele.game.common.avatar import Avatar
from bytele.game.common.enums import *
from bytele.game.common.map.game_board import GameBoard
from bytele.game.constants import *

class Client(UserClient):

def __init__(self):
    super().__init__()

def team_name(self) -> str:
    """
    Allows the team to set a team name.
    :return: Your team name
    """
    return "William Afton"

def take_turn(self, turn: int, world: GameBoard, avatar: Avatar) -> list[ActionType]:
    """
    This is where your AI will decide what to do.
    :param turn:        The current turn of the game.
    :param actions:     This is the actions object that you will add effort allocations or decrees to.
    :param world:       Generic world information
    """
    return []

