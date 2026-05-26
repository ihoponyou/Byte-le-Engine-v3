import random
from typing import override

from bytele.game.common.enums import ObjectType
from bytele.game.fnaacm.bots.general_bot_commands import *
# from bytele.game.common.map.game_board import GameBoard
# from bytele.game.controllers.movement_controller import MovementController
from bytele.game.fnaacm.bots.bot import Bot

class DumbBot(Bot):
    def __init__(self):
        super().__init__()
        self.object_type = ObjectType.DUMB_BOT
        self.vision_radius = 2
        self.boosted_vision_radius = 4
        #self.stun = False
