from __future__ import annotations

from datetime import date

from shared.deadline import resolve_deadline
from shared.schemas import PlannerTask


from __future__ import annotations

from datetime import date

from shared.deadline import resolve_deadline
from shared.schemas import PlannerTask


def fmt_deadline(phrase: str | None, today: date | None = None) -> str:
    """Date resolev """
    if not phrase or phrase.strip().lower() in {"without deadline", ""}:
        return "without deadline"
    resolved = resolve_deadline(phrase, today or date.today())
    return f"{phrase} ({resolved})" if resolved else phrase


def format_task(task: PlannerTask, today: date | None = None) -> str:
    lines = [
        f"<b>{task.title}</b>",
        f"Deadline: {fmt_deadline(task.deadline, today)}",
    ]
    if task.description:
        lines.append(f"\n{task.description}")

    if task.checkpoints:
        lines.append("\n<b>Plan:</b>")
        for i, cp in enumerate(task.checkpoints, 1):
            sub = ""
            if cp.deadline:
                sub = f" — <i>{fmt_deadline(cp.deadline, today)}</i>"
            lines.append(f"{i}. {cp.step}{sub}")

    if task.tags:
        lines.append("\n" + " ".join(f"#{t}" for t in task.tags))

    return "\n".join(lines)
