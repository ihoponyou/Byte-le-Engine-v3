import pygame as pyg

from bytele.visualizer.bytesprites.bytesprite import ByteSprite
from bytele.game.utils.vector import Vector
from bytele.visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory
from bytele.visualizer.config import PATH_TO_SPRITESHEETS


class DoorBS(ByteSpriteFactory):
    """
    Door ByteSprite Factory

    Sprite sheet row layout:
    0 -> CLOSED
    1 -> OPEN
    """

    PATH_TO_SPRITE = PATH_TO_SPRITESHEETS / 'Door.png'

    @staticmethod
    def update(
        data: dict,
        layer: int,
        pos: Vector,
        spritesheets: list[list[pyg.Surface]]
    ) -> list[pyg.Surface]:

        # Treat missing data as CLOSED
        if data.get('open', False) or data.get('state') == 'open':
            return spritesheets[1]

        return spritesheets[0]

    @staticmethod
    def create_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(
            screen,
            str(DoorBS.PATH_TO_SPRITE.resolve()),
            2,   # rows
            4,   # frames per row (even if static)
            DoorBS.update,
            colorkey=pyg.Color(255, 0, 255)
        )
