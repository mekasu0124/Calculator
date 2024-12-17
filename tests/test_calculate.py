from click.testing import CliRunner
from cli_app.commands.standard.calculate import calculate_command


def test_calculate_command():
    runner = CliRunner()
    result = runner.invoke(calculate_command, ["2", "3"])
    assert result.exit_code == 0
    assert "The sum of 2 and 3 is 5" in result.output
