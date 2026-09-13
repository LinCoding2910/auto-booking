import sys
from pathlib import Path

from dotenv import load_dotenv
from robot import run_cli


def main() -> None:
    load_dotenv()

    root = Path(__file__).resolve().parents[2]
    suite = root / "tests" / "recorded_test.robot"
    variable_file = root / "tests" / "variables.py"
    if not suite.exists():
        sys.exit(f"Suite not found: {suite}")

    run_cli(["--variablefile", str(variable_file), str(suite)])