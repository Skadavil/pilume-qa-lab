from copy import deepcopy
from datetime import UTC, datetime


events: list[dict[str, object]] = []


def record_event(action: str, state: dict[str, object]) -> None:
    event = {
        "timestamp": datetime.now(UTC).isoformat(),
        "action": action,
        "state": deepcopy(state),
    }

    events.append(event)


def read_events() -> list[dict[str, object]]:
    return deepcopy(events)
