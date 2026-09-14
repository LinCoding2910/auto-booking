"""Small Robot Framework library for starting a booking at its opening time."""

from datetime import datetime
from time import sleep
from zoneinfo import ZoneInfo


def wait_until_booking_opens(
    opens_at: str,
    timezone_name: str = "Asia/Kuala_Lumpur",
    poll_interval: float = 1.0,
) -> None:
    """Wait until ``opens_at`` before allowing the Robot test to continue.

    ``opens_at`` may be written as ``14/Sep/2026 08:00 AM`` or as an ISO
    datetime such as ``2026-09-14 08:00``. If the opening time has already
    passed, the function returns immediately.
    """
    if poll_interval <= 0:
        raise ValueError("poll_interval must be greater than zero")

    opening_time = _parse_opening_time(opens_at, timezone_name)
    while True:
        seconds_remaining = (opening_time - datetime.now(opening_time.tzinfo)).total_seconds()
        if seconds_remaining <= 0:
            return
        sleep(min(seconds_remaining, poll_interval))


def _parse_opening_time(opens_at: str, timezone_name: str) -> datetime:
    """Parse the configured time and attach the booking site's timezone."""
    try:
        timezone = ZoneInfo(timezone_name)
    except Exception as error:
        raise ValueError(f"Unknown timezone: {timezone_name}") from error

    for format_string in ("%d/%b/%Y %I:%M %p", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(opens_at, format_string).replace(tzinfo=timezone)
        except ValueError:
            continue

    raise ValueError(
        "opens_at must use 'DD/Mon/YYYY HH:MM AM/PM' or 'YYYY-MM-DD HH:MM'"
    )
