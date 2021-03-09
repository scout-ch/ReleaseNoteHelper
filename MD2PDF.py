import os
import mdpdf.cli as cli
from click.testing import CliRunner, Result

if os.path.exists("output.pdf"):
  os.remove("output.pdf")

# https://pypi.org/project/mdpdf/
runner: CliRunner = CliRunner()
result: Result = runner.invoke(cli.cli, ["-o", "output.pdf", "index.md"])