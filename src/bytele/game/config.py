import os
from typing import Any
import warnings
from pathlib import Path

from bytele.game.common.enums import *


warnings.simplefilter('ignore')

USE_PRECOMPILED_MAP = False
try:
    from bytele.game.map_data import USE_PRECOMPILED_MAP
except ImportError:
    # isn't this neat
    warnings.warn("map_data is missing; end-users may safely ignore this message")

"""
This file is important for configuring settings for the project. All parameters in this file have comments to explain 
what they do already. Refer to this file to clear any confusion, and make any changes as necessary.
"""

# Runtime settings / Restrictions --------------------------------------------------------------------------------------
# The engine requires these to operate
MAX_TICKS = 500                                     # max number of ticks the server will run regardless of game state
TQDM_BAR_FORMAT = "Game running at {rate_fmt} "     # how TQDM displays the bar
TQDM_UNITS = " turns"                               # units TQDM takes in the bar

MAX_SECONDS_PER_TURN = 0.1                          # max number of basic operations clients have for their turns

MAX_NUMBER_OF_ACTIONS_PER_TURN = 2                  # max number of actions per turn is currently set to 2

MIN_CLIENTS_START = None                            # minimum number of clients required to start running the game; should be None when SET_NUMBER_OF_CLIENTS is used
MAX_CLIENTS_START = None                            # maximum number of clients required to start running the game; should be None when SET_NUMBER_OF_CLIENTS is used
SET_NUMBER_OF_CLIENTS_START = 1                     # required number of clients to start running the game; should be None when MIN_CLIENTS or MAX_CLIENTS are used
CLIENT_KEYWORD = "client"                           # string required to be in the name of every client file, not found otherwise
CLIENT_DIRECTORY = "./"                             # location where client code will be found

MIN_CLIENTS_CONTINUE = None                         # minimum number of clients required to continue running the game; should be None when SET_NUMBER_OF_CLIENTS is used
MAX_CLIENTS_CONTINUE = None                         # maximum number of clients required to continue running the game; should be None when SET_NUMBER_OF_CLIENTS is used
SET_NUMBER_OF_CLIENTS_CONTINUE = 1                  # required number of clients to continue running the game; should be None when MIN_CLIENTS or MAX_CLIENTS are used

ALLOWED_MODULES = ["bytele.game.client.user_client",       # modules that clients are specifically allowed to access
                   "bytele.game.common.enums",
                   "bytele.game.common.game_object",
                   "bytele.game.constants",
                   "bytele.game.common.avatar",
                   "bytele.game.common.map.game_board",
                   "bytele.game.common.map.occupiable",
                   "bytele.game.utils.vector",
                   "typing",
                   "heapq",
                   "json",
                   "subprocess",
                   "math",
                   "numpy",
                   "scipy",
                   "pandas",
                   "itertools",
                   "functools",
                   "random",
                   ]

RESULTS_FILE_NAME = "results.json"                                  # Name and extension of results file
RESULTS_DIR = os.path.join(os.getcwd(), "logs")                     # Location of the results file
RESULTS_FILE = os.path.join(RESULTS_DIR, RESULTS_FILE_NAME)         # Results directory combined with file name

LOGS_FILE_NAME = 'turn_logs.json'
LOGS_DIR = os.path.join(os.getcwd(), "logs")                        # Directory for game log files
LOGS_FILE = os.path.join(LOGS_DIR, LOGS_FILE_NAME)

GAME_MAP_FILE_NAME = "game_map.json"                                # Name and extension of game file that holds generated world
GAME_MAP_DIR = os.path.join(os.getcwd(), "logs")                    # Location of game map file
GAME_MAP_FILEPATH = os.path.join(GAME_MAP_DIR, GAME_MAP_FILE_NAME)      # Filepath for game map file

class Debug:                    # Keeps track of the current debug level of the game
    level = DebugLevel.NONE

ROOT_DIR_NAME = 'Byte-le-Engine-v3'
PATH_TO_ROOT_DIR = Path()
PATH_TO_LDTK_PROJECT = str()
# this allows us to not ship the .ldtk file with the client package
if not USE_PRECOMPILED_MAP:
    parts = Path(__file__).parts
    root_idx = len(parts) - list(reversed(parts)).index(ROOT_DIR_NAME) 
    PATH_TO_ROOT_DIR = Path(*parts[:root_idx])
    PATH_TO_LDTK_PROJECT = str(PATH_TO_ROOT_DIR / 'map.ldtk') # uber chopped but works

class LDtkIdentifier(str, Enum):
    """
    Level, entity, and enum identifiers in our LDtk project currently use PascalCase.
    Python enum members use UPPER_CASE.

    By overriding `_generate_next_value`, we can define identifiers using Python convention
    and have their values close to our LDtk convention.
    """
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        # Future projects may simply use UPPER_CASE in LDtk identifiers and simply return the name as-is.
        return name.lower().replace('_', '')

class LDtk:
    class CollisionType:
        # should mirror values in LDtk editor
        NONE = 0
        WALL = 1
        SHADOW = 5
    class EntityIdentifier(LDtkIdentifier):
        DOOR = auto()
        GENERATOR = auto()
        CHARACTER_START = auto()
        COIN_SPAWNER = auto()
    class LayerIdentifier(LDtkIdentifier):
        ENTITIES = auto()
        COLLISIONS = auto()
    class LevelIdentifier(LDtkIdentifier):
        PRODUCTION = auto()
        TEST = auto()
    class SpawnedEntityType(LDtkIdentifier):
        PLAYER = auto()

# Other Settings Here --------------------------------------------------------------------------------------------------

