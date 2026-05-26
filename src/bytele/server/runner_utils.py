import logging
from queue import Queue
from bytele.server.database import SessionLocal
from bytele.server.models.run import Run
from bytele.server.models.tournament import Tournament
from bytele.server.models.turn import Turn
from bytele.server.models.submission_run_info import SubmissionRunInfo
from bytele.server.models.team import Team
from bytele.server.models.team_type import TeamType
from bytele.server.models.university import University
from bytele.server.models.submission import Submission
from bytele.server.enums import RunnerOptions

import sys
import subprocess


class DB:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        self.db.begin()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


def worker_main(jobqueue: Queue):
    while not jobqueue.empty():
        job = jobqueue.get()
        func = job[0]
        args = job[1:]
        logging.debug(f'running {func.__name__}({args})')
        func(*args)
        jobqueue.task_done()


def run_runner(working_directory: str, runner_option: RunnerOptions, seed: int | None = None) -> bytes:
    """
    runs a script in the runner folder.
    end path is where the runner is located
    runner is the name of the script (no extension)
    """
    cmd: list[str] = [sys.executable, "launcher.pyz"]
    if runner_option == RunnerOptions.GENERATE:
        cmd += ['generate']
        if seed is not None:
            cmd += ['-s', f'{seed}']
    elif runner_option == RunnerOptions.RUN:
        cmd += ['run', '-q']
    elif runner_option == RunnerOptions.VISUALIZE:
        cmd += ['v', '-log', 'logs', '-end_time', '5', '-skip_start', '-fullscreen', '-playback_speed', '2.0']
    elif runner_option == RunnerOptions.VERSION:
        cmd += ['version']
    else:
        raise Exception("Not Implemented")

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=working_directory)
    stdout, stderr = p.communicate()
    p.wait()
    return stdout
