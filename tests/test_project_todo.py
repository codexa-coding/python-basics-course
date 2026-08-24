import pytest

from python_basics.project_todo import (
    add_task,
    complete_task,
    format_tasks,
    remove_task,
)


def test_add_and_format_task() -> None:
    tasks = []

    add_task(tasks, " Learn Python ")

    assert tasks == [{"title": "Learn Python", "completed": False}]
    assert format_tasks(tasks) == "1. [ ] Learn Python"


def test_complete_task() -> None:
    tasks = [{"title": "Write tests", "completed": False}]

    complete_task(tasks, 1)

    assert tasks[0]["completed"] is True


def test_remove_task() -> None:
    tasks = [
        {"title": "First task", "completed": False},
        {"title": "Second task", "completed": False},
    ]

    removed = remove_task(tasks, 1)

    assert removed["title"] == "First task"
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Second task"


def test_invalid_task_number_raises_error() -> None:
    with pytest.raises(IndexError):
        complete_task([], 1)
