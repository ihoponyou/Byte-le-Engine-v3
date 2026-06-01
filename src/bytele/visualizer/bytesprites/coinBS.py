import os
import pygame as pyg

from bytele.visualizer.bytesprites.bytesprite import ByteSprite
from bytele.game.utils.vector import Vector
from bytele.game.common.enums import ObjectType
from bytele.visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory
from bytele.visualizer.config import PATH_TO_STATICSPRITES


class CoinBS(ByteSpriteFactory):
    """
    Static Coin bytesprite using Coin.png.
    """

    PATH_TO_SPRITE = PATH_TO_STATICSPRITES / 'Coin.png'

    @staticmethod
    def update(
        data: dict,
        layer: int,
        pos: Vector,
        spritesheets: list[list[pyg.Surface]]
    ) -> list[pyg.Surface]:
        if data['state'] != 'idle':
            return spritesheets[1]
        return spritesheets[0]

    @staticmethod
    def create_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(
            screen,
            str(CoinBS.PATH_TO_SPRITE.resolve()),
            2,
            ObjectType.COIN_SPAWNER.value,                  # object type (match Adapter)
            CoinBS.update,
            colorkey=None       # use PNG alpha transparency
        )
