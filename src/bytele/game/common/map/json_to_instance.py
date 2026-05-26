from typing import Type

from bytele.game.common.avatar import Avatar
from bytele.game.common.enums import ObjectType
from bytele.game.common.game_object import GameObject
from bytele.game.common.map.wall import Wall
from bytele.game.common.stations.occupiable_station import OccupiableStation
from bytele.game.common.stations.refuge import Refuge
from bytele.game.common.stations.station import Station
from bytele.game.fnaacm.bots.crawler_bot import CrawlerBot
from bytele.game.fnaacm.bots.dumb_bot import DumbBot
from bytele.game.fnaacm.bots.ian_bot import IANBot
from bytele.game.fnaacm.bots.jumper_bot import JumperBot
from bytele.game.fnaacm.bots.support_bot import SupportBot
from bytele.game.fnaacm.map.coin_spawner import CoinSpawner
from bytele.game.fnaacm.map.door import Door
from bytele.game.fnaacm.map.vent import Vent
from bytele.game.fnaacm.stations.battery_spawner import BatterySpawner
from bytele.game.fnaacm.stations.generator import Generator
from bytele.game.fnaacm.stations.scrap_spawner import ScrapSpawner


OBJECT_TYPE_TO_CLASS: dict[ObjectType, Type] = {
    ObjectType.AVATAR: Avatar,
    ObjectType.BATTERY_SPAWNER: BatterySpawner,
    ObjectType.COIN_SPAWNER: CoinSpawner,
    ObjectType.DOOR: Door,
    ObjectType.GENERATOR: Generator,
    ObjectType.OCCUPIABLE_STATION: OccupiableStation,
    ObjectType.REFUGE: Refuge,
    ObjectType.SCRAP_SPAWNER: ScrapSpawner,
    ObjectType.STATION: Station,
    ObjectType.VENT: Vent,
    ObjectType.WALL: Wall,
    ObjectType.CRAWLER_BOT: CrawlerBot,
    ObjectType.DUMB_BOT: DumbBot,
    ObjectType.IAN_BOT: IANBot,
    ObjectType.JUMPER_BOT: JumperBot,
    ObjectType.SUPPORT_BOT: SupportBot
}
def json_to_instance(data: dict) -> GameObject:
    obj_type = ObjectType(data['object_type'])
    return OBJECT_TYPE_TO_CLASS[obj_type]().from_json(data)
