import asyncio
import json
import typing
from app.gsheets import append_sheet_data, get_sheet_first_row, has_sheet_header_row
from app.habitica import get_habitica_tasks, HabiticaTask
from app.config import config

DATE_COMPLETED_COL_IDX = config.HABITICA_GSHEET_COLUMNS.index(
    ("date_completed", "dateCompleted")
)
GSHEET_HEADER = [col_name for col_name, _ in config.HABITICA_GSHEET_COLUMNS]


def build_habitica_data_for_gsheet(
    tasks: list[HabiticaTask],
    should_contain_header: bool = True,
) -> list[list[str | int | float]]:
    rows: list[list[typing.Any]] = [GSHEET_HEADER] if should_contain_header else []

    for task in tasks:
        row: list[typing.Any] = []
        for _, key in config.HABITICA_GSHEET_COLUMNS:
            value: str | int | float | list[typing.Any] | None = task.get(key, "")

            if value is None:
                value = ""

            if isinstance(value, list) or isinstance(value, dict):
                value = json.dumps(value)

            row.append(value)
        rows.append(row)

    return rows


async def main():
    first_gsheet_row = await get_sheet_first_row(sheet_name="db")
    _has_sheet_header_row = await has_sheet_header_row(
        sheet_name="db", header_data=GSHEET_HEADER
    )
    date_completed = (
        first_gsheet_row[DATE_COMPLETED_COL_IDX]
        if first_gsheet_row is not None
        else None
    )
    completed_habitica_tasks = await get_habitica_tasks(type="completedTodos")
    completed_habitica_tasks_list = build_habitica_data_for_gsheet(
        tasks=completed_habitica_tasks,
        should_contain_header=False if _has_sheet_header_row else True,
    )
    filtered_completed_habitica_tasks_list = [
        row
        for row in completed_habitica_tasks_list
        if date_completed is None or row[DATE_COMPLETED_COL_IDX] > date_completed
    ]

    await append_sheet_data(
        sheet_name="db",
        values=filtered_completed_habitica_tasks_list,
        start_range="A2" if _has_sheet_header_row else "A1",
    )


if __name__ == "__main__":
    asyncio.run(main())
