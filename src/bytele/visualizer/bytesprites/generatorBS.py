import os
import pygame as pyg

from bytele.game.common.enums import ObjectType
from bytele.visualizer.bytesprites.bytesprite import ByteSprite
from bytele.game.utils.vector import Vector
from bytele.visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory


class GeneratorBS(ByteSpriteFactory):
    """
    Generator bytesprite using Generator.png.
    """

    GENERATOR_PATH = os.path.join(
        os.getcwd(),
        'visualizer/images/staticsprites/Generator.png'
    )

    @staticmethod
    def update(
        data: dict,
        layer: int,
        pos: Vector,
        spritesheets: list[list[pyg.Surface]]
    ) -> list[pyg.Surface]:
        if data.get('active', False):
            return spritesheets[1]
        return spritesheets[0]

    @staticmethod
    def create_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(
            screen,
            GeneratorBS.GENERATOR_PATH,
            2,
            ObjectType.GENERATOR.value,                  # object type (match Adapter)
            GeneratorBS.update,
            colorkey=None       # use PNG alpha transparency
        )
