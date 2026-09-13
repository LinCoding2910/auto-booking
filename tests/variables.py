from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def get_variables():
    return {
        "MEMBERSHIP_NO": environ.get("MEMBERSHIP_NO"),
        "PASSWORD": environ.get("PASSWORD"),
    }