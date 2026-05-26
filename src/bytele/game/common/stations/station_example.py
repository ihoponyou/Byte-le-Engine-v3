from bytele.game.common.avatar import Avatar
from bytele.game.common.enums import ObjectType
from bytele.game.common.items.item import Item
from bytele.game.common.stations.station import Station


# create example of station that gives item to avatar
class StationExample(Station):
    def __init__(self, held_item: Item | None = None):
        super().__init__(held_item=held_item)
        self.object_type = ObjectType.STATION_EXAMPLE

    def take_action(self, avatar: Avatar) -> Item | None:
        """
            In this example of what a station could do, the avatar picks up the item from this station to show the
            station's purpose.
            :param avatar:
            :return:
        """
        avatar.pick_up(self.held_item)
