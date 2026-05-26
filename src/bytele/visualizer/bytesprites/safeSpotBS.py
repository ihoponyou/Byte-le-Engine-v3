import os
import pygame as pyg

from bytele.visualizer.bytesprites.bytesprite import ByteSprite
from bytele.game.utils.vector import Vector
from bytele.visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory
from bytele.game.common.enums import ObjectType


class SafeSpotBS(ByteSpriteFactory):
    """
    Static safe spot bytesprite using SafeSpot.png.
    """

    SAFESPOT_PATH = os.path.join(
        os.getcwd(),
        'visualizer/images/staticsprites/SafeSpot.png'
    )

    @staticmethod
    def update(
        data: dict,
        layer: int,
        pos: Vector,
        spritesheets: list[list[pyg.Surface]]
    ) -> list[pyg.Surface]:
        if data.get('is_closed', False):
            return spritesheets[0]
        return spritesheets[1]

    @staticmethod
    def create_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(
            screen,
            SafeSpotBS.SAFESPOT_PATH,
            2,
            ObjectType.REFUGE.value, # must match Adapter + logs
            SafeSpotBS.update,
            colorkey=None               # use PNG alpha transparency
        )
