from typing import List, Optional, override
from bytele.game.fnaacm.bots.bot import Bot
from bytele.game.common.enums import ActionType, ObjectType
from bytele.game.utils.vector import Vector
from bytele.game.controllers.pathfind_controller import a_star_path


class IANBot(Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_type = ObjectType.IAN_BOT
        self.turn_delay = 2  # moves every 2 turns
        self.vision_radius = 30
        self.boosted_vision_radius = 40
