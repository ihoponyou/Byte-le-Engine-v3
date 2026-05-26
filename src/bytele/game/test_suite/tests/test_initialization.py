import unittest

from bytele.game.common.enums import ObjectType
from bytele.game.common.avatar import Avatar
from bytele.game.common.items.item import Item
from bytele.game.common.stations.station import Station
from bytele.game.common.stations.occupiable_station import OccupiableStation
from bytele.game.common.map.tile import Tile
from bytele.game.common.map.wall import Wall
from bytele.game.utils.vector import Vector


class TestInitialization(unittest.TestCase):
    """
    `Test Avatar Notes:`

        This class tests the instantiation of different Objects within the project. Recall that every new class created
        needs a respective ObjectType enum created for it.
    """

    def setUp(self) -> None:
        self.item: Item = Item(10, 100)
        self.avatar: Avatar = Avatar(None)
        self.station: Station = Station(None)
        self.occupiable_station: OccupiableStation = OccupiableStation(None)
        self.tile: Tile = Tile()
        self.wall: Wall = Wall()
        self.vector: Vector = Vector()

    # tests that all objects have the correct ObjectType
    def test_object_init(self):
        self.assertEqual(self.item.object_type, ObjectType.ITEM)
        self.assertEqual(self.avatar.object_type, ObjectType.AVATAR)
        self.assertEqual(self.station.object_type, ObjectType.STATION)
        self.assertEqual(self.occupiable_station.object_type, ObjectType.OCCUPIABLE_STATION)
        self.assertEqual(self.tile.object_type, ObjectType.TILE)
        self.assertEqual(self.wall.object_type, ObjectType.WALL)
        self.assertEqual(self.vector.object_type, ObjectType.VECTOR)
