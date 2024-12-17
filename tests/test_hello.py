from click.testing import CliRunner
from cli_app.commands.general.hello import hello_command


def test_hello_command():
    runner = CliRunner()
    result = runner.invoke(hello_command, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output
