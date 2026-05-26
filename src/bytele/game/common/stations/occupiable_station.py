from typing import Self


from bytele.game.common.map.occupiable import Occupiable
from bytele.game.common.enums import ObjectType
from bytele.game.common.items.item import Item
from bytele.game.common.stations.station import Station


# create station object that contains occupied_by
class OccupiableStation(Occupiable, Station):
    """
    `OccupiableStation Class Notes:`

        Occupiable Station objects inherit from both the Occupiable and Station classes. This allows for other
        objects to be "on top" of the Occupiable Station. For example, an Avatar object can be on top of this object.
        Since Stations can contain items, items can be stored in this object too.

        Any GameObject or Item can be in an Occupiable Station.

        Occupiable Station Example is a small file that shows an example of how this class can be
        used. The example class can be deleted or expanded upon if necessary.
    """
    def __init__(self, held_item: Item | None = None):
        super().__init__(held_item=held_item)
        self.object_type: ObjectType = ObjectType.OCCUPIABLE_STATION
        self.held_item = held_item

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self
