from bytele.server.schemas.team.team_base import TeamBase
from bytele.server.schemas.team_type.team_type_base import TeamTypeBase


class TeamTypeSchema(TeamTypeBase):
    """
    Schema for TeamType using TeamTypeBase and includes its relations.
    """
    teams: list[TeamBase]
