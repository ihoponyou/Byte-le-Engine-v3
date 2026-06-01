import os
import pygame as pyg

from bytele.game.common.enums import ObjectType
from bytele.visualizer.bytesprites.bytesprite import ByteSprite
from bytele.game.utils.vector import Vector
from bytele.visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory
from bytele.visualizer.config import PATH_TO_STATICSPRITES


class TileBS(ByteSpriteFactory):
    """
    Static Tile bytesprite using Tile.png.
    """

    TILE_PATH = PATH_TO_STATICSPRITES / 'Tile.png'

    @staticmethod
    def update(
        data: dict,
        layer: int,
        pos: Vector,
        spritesheets: list[list[pyg.Surface]]
    ) -> list[pyg.Surface]:
        # Static sprite: always use first row
        return spritesheets[0]

    @staticmethod
    def create_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(
            screen,
            str(TileBS.TILE_PATH.resolve()),
            1,                  # one row for static tile
            ObjectType.TILE.value,                  # object type (match Adapter)
            TileBS.update,
            colorkey=None       # use PNG alpha for transparency
        )
