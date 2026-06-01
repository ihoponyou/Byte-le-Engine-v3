from bytele.game.common.avatar import Avatar
from bytele.game.common.game_object import GameObject
from bytele.game.common.map.game_board import GameBoard
from bytele.game.common.map.wall import Wall
from bytele.game.common.map.door import Door
from bytele.game.common.map.coin_spawner import CoinSpawner
from bytele.game.ldtk.ldtk_json import EntityInstance, LayerInstance, LdtkJSON, Level 
from bytele.game.config import LDtk
from bytele.game.utils.helpers import read_json_file
from bytele.game.utils.vector import Vector


ENTITY_LOAD_PRIORITY: dict[str, int] = {
    LDtk.EntityIdentifier.DOOR: -9999, # load doors at least before generators
}
"""
unspecified entities have a default priority of 0
highest = first; lowest = last
"""

def get_entity_load_priority(entity: EntityInstance) -> int:
    return ENTITY_LOAD_PRIORITY.get(entity.identifier.lower(), 0)

def _get_character_from_start(character_start: EntityInstance) -> GameObject:
    spawned_entity: GameObject | None = None
    parsed_value: str = ''
    for field in character_start.field_instances:
        if field.identifier.lower() != 'character_to_spawn':
            continue

        parsed_value = field.value
        match field.value.lower():
            case LDtk.SpawnedEntityType.PLAYER:
                spawned_entity = Avatar()
            case _:
                raise ValueError(f'unhandled spawner entity type: "{field.value}"')

    if spawned_entity is None:
        raise RuntimeError(f'could not determine spawner\'s entity type; best guess is "{parsed_value}"')

    return spawned_entity

def load_entities(locations: dict[Vector, list[GameObject]], entity_layer: LayerInstance):
    doors: dict[str, Door] = {}
    sorted_entities = sorted(entity_layer.entity_instances, key=get_entity_load_priority)
    for entity in sorted_entities:
        game_object: GameObject
        match entity.identifier.lower():
            case LDtk.EntityIdentifier.DOOR:
                game_object = Door()
                doors[entity.iid] = game_object
            case LDtk.EntityIdentifier.COIN_SPAWNER:
                game_object = CoinSpawner.from_ldtk_entity(entity)
            case LDtk.EntityIdentifier.CHARACTER_START:
                game_object = _get_character_from_start(entity)
            case _:
                raise ValueError(f'unhandled entity identifier: "{entity.identifier}"')

        position = Vector(entity.grid[0], entity.grid[1])
        GameBoard.insert_location(locations, position, game_object)

def load_collisions(locations: dict[Vector, list[GameObject]], collision_layer: LayerInstance, map_width: int):
    for i in range(len(collision_layer.int_grid_csv)):
        position = Vector(i % map_width, i // map_width)
        game_object: GameObject | None = None 
        collision_type = collision_layer.int_grid_csv[i]
        match collision_type:
            case LDtk.CollisionType.NONE:
                pass
            case LDtk.CollisionType.WALL:
                game_object = Wall()
            case LDtk.CollisionType.SHADOW:
                game_object = Wall(use_shadow_sprite=True)
            case _:
                raise ValueError(f'unhandled collision type: {collision_type}')

        if game_object is None:
            continue
        GameBoard.insert_location(locations, position, game_object)

def map_data_from_ldtk_file(path_to_ldtk_file: str, level_identifier: str = LDtk.LevelIdentifier.PRODUCTION):
    json_data: dict = read_json_file(path_to_ldtk_file)
    return map_data_from_ldtk_dict(json_data, level_identifier)

def map_data_from_ldtk_dict(ldtk_dict: dict, level_identifier: str = LDtk.LevelIdentifier.PRODUCTION):
    ldtk_json: LdtkJSON = LdtkJSON.from_dict(ldtk_dict)
    return map_data_from_ldtk_json(ldtk_json, level_identifier)

def map_data_from_ldtk_json(ldtk_json: LdtkJSON, level_identifier: str = LDtk.LevelIdentifier.PRODUCTION) -> tuple[dict[Vector, list[GameObject]], Vector]:
    """
    :param level_identifier: case-insensitive identifier of the level to parse
    :return: a tuple containing a Locations dict as used in GameBoard and the size of the map
    """
    assert len(ldtk_json.levels) >= 1, f'no levels found'
    level: Level | None = None
    for l in ldtk_json.levels:
        if l.identifier.lower() == level_identifier.lower():
            level = l
            break
    assert not (level is None), f'no level found with identifier "{level_identifier}"'

    layers = level.layer_instances
    if layers is None:
        raise RuntimeError(f'layers of level "{level.identifier}" could not be found; check if LDtk project setting "Save levels separately" is enabled')
    if len(layers) < 1:
        raise RuntimeError(f'level "{level.identifier}" has no layers')

    map_size = Vector(layers[0].c_wid, layers[0].c_hei)
    locations: dict[Vector, list[GameObject]] = {}
    for layer in layers:
        match layer.identifier.lower():
            case LDtk.LayerIdentifier.ENTITIES:
                load_entities(locations, layer)
            case LDtk.LayerIdentifier.COLLISIONS:
                load_collisions(locations, layer, map_size.x)
            case 'AutoLayer':
                pass
            case _:
                raise ValueError(f'unhandled layer: {layer.identifier}')

    return locations, map_size
