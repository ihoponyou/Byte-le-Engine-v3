from typing import Type

from bytele.game.common.avatar import Avatar
from bytele.game.common.enums import ObjectType
from bytele.game.common.game_object import GameObject
from bytele.game.common.map.wall import Wall
from bytele.game.common.map.occupiable_station import OccupiableStation
from bytele.game.common.map.station import Station
from bytele.game.common.map.door import Door
from bytele.game.common.map.coin_spawner import CoinSpawner


OBJECT_TYPE_TO_CLASS: dict[ObjectType, Type] = {
    ObjectType.AVATAR: Avatar,
    ObjectType.DOOR: Door,
    ObjectType.COIN_SPAWNER: CoinSpawner,
    ObjectType.OCCUPIABLE_STATION: OccupiableStation,
    ObjectType.STATION: Station,
    ObjectType.WALL: Wall,
}
def json_to_instance(data: dict) -> GameObject:
    obj_type = ObjectType(data['object_type'])
    return OBJECT_TYPE_TO_CLASS[obj_type]().from_json(data)
