# Project Management CLI

A simple command-line project manager built in Python cli project for managing users, projects, and tasks. 
## Features

- Add users with name and email validation
- Add projects with title, description, due date, and user ownership
- Add tasks linked to a project
- List users, tasks, and full project/task summaries
- Mark task status in the data model and calculate overdue projects

## Project Structure

- `main.py` - CLI entry point using `click` and `rich`
- `models/user.py` - `User` and `Person` models with email validation and serialization
- `models/project.py` - `Project` model with due date parsing, overdue detection, and task relationships
- `models/task.py` - `Task` model with status validation and serialization
- `utils/file_io.py` - JSON persistence for users, projects, and tasks
- `data.json` - runtime storage of persisted data
- `tests/` - unit tests for models


## Usage

Run the CLI from the repository root:

python3 main.py --help

Available commands:

- `add-user` - Create a new user
- `list-users` - Show all users
- `add-project` - Create a new project for an existing user
- `add-task` - Create a new task under an existing project
- `list-tasks` - Show all tasks or tasks for a specific project
- `list-all` - Display users, projects, and tasks in one report


## Data Persistence

- `data.json` stores persisted `users`, `projects`, and `tasks`.
- The application loads from this file on startup and writes back after add operations.
- If `data.json` is missing or corrupted, the CLI starts with empty data and recreates the file when saving.

## Testing

Run unit tests with Python's unittest:

## Tech-stack
python