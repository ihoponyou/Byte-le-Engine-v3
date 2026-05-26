from typing import List, Optional, override
from bytele.game.common.enums import ObjectType
from bytele.game.fnaacm.bots.bot import Bot
# from bytele.game.common.enums import ActionType
# from bytele.game.utils.vector import Vector
# from bytele.game.controllers.pathfind_controller import a_star_path


class CrawlerBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_type = ObjectType.CRAWLER_BOT
        self.turn_delay = 4  # moves every 4 turns unboosted
        self.vision_radius = 30
        self.boosted_vision_radius = 40
