from __future__ import annotations

from bytele.server.schemas.run.run_base import RunBase
from bytele.server.schemas.submission_run_info.submission_run_info_w_submission import SubmissionRunInfoWSubmission
from bytele.server.schemas.turn.turn_schema import TurnBase


class RunSchemaWithoutTournament(RunBase):
    """
    Schema for Run using RunBase. Includes its relations to other tables EXCEPT tournament.
    """
    submission_run_infos: list[SubmissionRunInfoWSubmission]
