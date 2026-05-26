from bytele.server.schemas.run.run_base import RunBase
from bytele.server.schemas.turn.turn_base import TurnBase


class TurnSchema(TurnBase):
    """
    Schema for Turn using TurnBase and includes its relations.
    """
    run: RunBase
