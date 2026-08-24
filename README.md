# Python Basics Course Repository

A practical, beginner-friendly repository for learning core Python concepts through:

- Short, runnable lessons
- Hands-on exercises
- Reference solutions
- Automated tests
- A small command-line To-Do application project

## Prerequisites

Install Python 3.11 or newer.

Check your installed version:

```console
python --version
```

## Setup

1. Clone or download the repository

```console
git clone <your-repository-url>
cd python-basics-course
```

2. Create a virtual environment

A virtual environment keeps project dependencies separate from your global Python installation.
bash

```console
python -m venv .venv
```
Activate it:

macOS / Linux
```console
source .venv/bin/activate
```

Windows PowerShell
```console
.venv\Scripts\Activate.ps1
```

Windows Command Prompt
```console
.venv\Scripts\activate.bat
```

3. Install development dependencies
```console
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Course roadmap

| Lesson | Topic | Main concepts |
| --- | --- | --- |
| 1	| Variables and types	| strings, numbers, booleans, input, conversion |
| 2	| Control flow | comparisons, conditionals, loops |
| 3 |	Collections |	lists, tuples, dictionaries, sets |
| 4 |	Functions |	parameters, return values, scope, type hints |
| 5	| Files and errors | reading files, writing files, exceptions |
| Project	| To-Do CLI |	combining the concepts into a usable application |

## Run the lessons

Run any lesson as a module from the repository root:

```console
python -m python_basics.lesson_01_variables
python -m python_basics.lesson_02_control_flow
python -m python_basics.lesson_03_collections
python -m python_basics.lesson_04_functions
python -m python_basics.lesson_05_files_and_errors
```

## Complete excercises

Open the matching file under `exercises/`.

Example:
```console
python exercises/01_variables_exercises.py
```

Replace `pass` with your implementation. You can compare your work against the corresponding file under `solutions/`.

## Run tests

Tests validate the examples and the final project:

```console
pytest
```

Run a single test file:
```console
pytest tests/test_lesson_03_collections.py
```

## Run the To-Do application

```console
python -m python_basics.project_todo
```

Commands available in the application:

```console
add <task description>
list
done <task number>
remove <task number>
help
quit
```

## Recommended learning process

1. Read one lesson.
2. Run the example code.
3. Change values and observe the output.
4. Complete the exercise without looking at the solution.
5. Run the tests.
6. Continue to the next lesson.
7. Build or extend the To-Do application.

## Useful Python conventions

- Use `snake_case` for variables and functions.
- Use `PascalCase` for class names.
- Prefer descriptive names such as `total_price` rather than `x`.
- Write small functions with one responsibility.
- Add type hints to clarify expected values.
- Catch specific exceptions rather than using a bare `except`.

