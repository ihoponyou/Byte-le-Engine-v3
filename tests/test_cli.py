from typer.testing import CliRunner

from bytele.cli import app
from bytele.server.enums import e_TeamType, e_University

runner = CliRunner()


def test_game_generate():
    result = runner.invoke(app, ['game', '-g'])
    assert result.exit_code == 0
    assert 'generating' in result.output.lower()

def test_register():
    team_name = 'mymegalongteamname'
    team_type = e_TeamType.UNDERGRADUATE
    university = e_University.NDSU
    result = runner.invoke(app, ['register'], input=f'{team_name}\n{team_type.value}\n{university.value}')
    assert result.exit_code == 0
    assert 'register' in result.output
