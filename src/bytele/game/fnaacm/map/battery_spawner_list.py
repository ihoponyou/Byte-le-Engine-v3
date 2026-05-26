from bytele.game.fnaacm.game_object_list import GameObjectList
from bytele.game.fnaacm.stations.battery_spawner import BatterySpawner


class BatterySpawnerList(GameObjectList[BatterySpawner]):
    def __init__(self):
        super().__init__('batteries', BatterySpawner)
