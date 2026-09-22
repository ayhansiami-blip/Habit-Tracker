# Habit Tracker

A simple command-line habit tracker built with Python.
The project allows users to create, view, search, complete, and delete habits while keeping track of daily completion and streaks.

## Features

* Add new habits with optional notes
* View all saved habits
* Search for a specific habit
* Mark habits as completed for the current day
* Track consecutive-day streaks
* Delete habits
* View basic statistics
* Automatically save data using a JSON file
* Automatically update daily completion status when the program starts

## How It Works

Each habit stores information such as:

* **Name** — The name of the habit
* **Completed** — Whether the habit has been completed today
* **Last completed** — The date the habit was last completed
* **Streak** — The number of consecutive days the habit has been completed
* **Note** — Optional additional information about the habit

The program uses the current date to determine whether a habit was completed today.

### Streak System

When a habit is ticked:

* If it has never been completed, its streak starts at `1`.
* If it was completed yesterday, the streak increases by `1`.
* If it was already completed today, the streak stays unchanged.
* If it was last completed before yesterday, the streak resets to `1`.

## Data Storage

Habit data is stored locally in:

```text
habits.json
```

The program uses Python's built-in `json` module to save and load the habits.

Dates are stored as strings in ISO format, for example:

```text
2026-09-23
```

When the program needs to compare a stored date with today's date, the string is converted back into a Python `date` object.

## Requirements

* Python 3.x

No external Python packages are required.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/ayhansiami-blip/Habit-Tracker.git
```

Move into the project directory:

```bash
cd Habit-Tracker
```

Run the program:

```bash
python main.py
```

## Project Structure

```text
Habit-Tracker/
│
├── main.py
├── habits
```
