import unittest

from bytele.game.common.map.tile import Tile
from bytele.game.common.map.wall import Wall
from bytele.game.common.stations.station import Station
from bytele.game.common.stations.occupiable_station import OccupiableStation
from bytele.game.common.avatar import Avatar
from bytele.game.common.enums import ObjectType


class TestTile(unittest.TestCase):
    """
    `Test Tile Notes:`

        This class tests the different methods in the Tile class.
    """
    def setUp(self) -> None:
        self.tile: Tile = Tile()
        self.wall: Wall = Wall()
        self.station: Station = Station()
        self.occupiable_station: OccupiableStation = OccupiableStation()
        self.avatar: Avatar = Avatar()

    # test json method
    def test_tile_json(self):
        data: dict = self.tile.to_json()
        tile: Tile = Tile().from_json(data)
        self.assertEqual(self.tile.object_type, tile.object_type)
