"""
Mini project: a command-line To-Do application.

This project combines:
- lists
- dictionaries
- functions
- loops
- conditionals
- input validation
"""

from typing import TypedDict


class TodoItem(TypedDict):
    title: str
    completed: bool


def create_task(title: str) -> TodoItem:
    """Create one normalized task dictionary."""
    cleaned_title = title.strip()

    if not cleaned_title:
        raise ValueError("A task title cannot be empty.")

    return {"title": cleaned_title, "completed": False}


def add_task(tasks: list[TodoItem], title: str) -> None:
    """Add a task to the list."""
    tasks.append(create_task(title))


def complete_task(tasks: list[TodoItem], task_number: int) -> None:
    """Mark a one-based task number as complete."""
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        raise IndexError("Task number does not exist.")

    tasks[index]["completed"] = True


def remove_task(tasks: list[TodoItem], task_number: int) -> TodoItem:
    """Remove and return a task by its one-based task number."""
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        raise IndexError("Task number does not exist.")

    return tasks.pop(index)


def format_tasks(tasks: list[TodoItem]) -> str:
    """Create a readable numbered task list."""
    if not tasks:
        return "No tasks available."

    lines = []

    for index, task in enumerate(tasks, start=1):
        status = "x" if task["completed"] else " "
        lines.append(f"{index}. [{status}] {task['title']}")

    return "\n".join(lines)


def print_help() -> None:
    """Print supported commands."""
    print(
        """
Commands:
  add <task description>  Add a new task
  list                    Show all tasks
  done <task number>      Mark a task as completed
  remove <task number>    Delete a task
  help                    Show this help message
  quit                    Exit the application
""".strip()
    )


def main() -> None:
    """Run the interactive command-line application."""
    tasks: list[TodoItem] = []

    print("Welcome to the Python To-Do App.")
    print_help()

    while True:
        raw_command = input("\n> ").strip()

        if not raw_command:
            continue

        command, *arguments = raw_command.split(maxsplit=1)
        command = command.lower()

        try:
            if command == "add":
                if not arguments:
                    raise ValueError("Provide a task description after 'add'.")

                add_task(tasks, arguments[0])
                print("Task added.")

            elif command == "list":
                print(format_tasks(tasks))

            elif command == "done":
                if not arguments:
                    raise ValueError("Provide a task number after 'done'.")

                complete_task(tasks, int(arguments[0]))
                print("Task completed.")

            elif command == "remove":
                if not arguments:
                    raise ValueError("Provide a task number after 'remove'.")

                removed_task = remove_task(tasks, int(arguments[0]))
                print(f"Removed: {removed_task['title']}")

            elif command == "help":
                print_help()

            elif command in {"quit", "exit"}:
                print("Goodbye.")
                break

            else:
                print("Unknown command. Type 'help' to see available commands.")

        except ValueError as error:
            print(f"Input error: {error}")
        except IndexError as error:
            print(f"Task error: {error}")


if __name__ == "__main__":
    main()
