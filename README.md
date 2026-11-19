# 🏏 Fantasy Cricket League Management System

A Python-based Fantasy Cricket League Management System that allows users to manage cricket players, create fantasy teams, validate team selections, and rank teams based on their total credits.

This project is built using **Object-Oriented Programming (OOP)** and Python's built-in CSV module. It focuses on writing clean, modular, and reusable Python code while applying real-world programming concepts.

## 🚀 Project Features

- **Player Management:** Load and manage cricket player information from CSV files.
- **Fantasy Team Creation:** Create teams with selected players, a captain, and a vice-captain.
- **Team Validation:** Check whether teams follow the fantasy league rules.
- **Duplicate Player Detection:** Identify repeated players in a fantasy team.
- **Credit Calculation:** Calculate total credits and remaining credits for each team.
- **Role Distribution:** Count players according to their cricketing roles.
- **Franchise Distribution:** Track the number of players selected from each franchise.
- **League Management:** Add and manage multiple fantasy teams.
- **Team Ranking:** Rank teams according to their total credits.
- **CSV Data Loading:** Read player and team information using Python's `csv.DictReader()`.

## 📋 Fantasy League Rules

Every fantasy team must follow these rules:

| Rule                | Requirement                                |
| ------------------- | ------------------------------------------ |
| Total Players       | Exactly 11 players                         |
| Maximum Credits     | 100 credits                                |
| Wicket Keepers (WK) | 1–2 players                                |
| Batsmen (BAT)       | 3–5 players                                |
| All-Rounders (AR)   | 1–3 players                                |
| Bowlers (BOWL)      | 3–5 players                                |
| Franchise Limit     | Maximum 7 players from one franchise       |
| Captain             | Must belong to the selected team           |
| Vice-Captain        | Must belong to the selected team           |
| Captain Selection   | Captain and vice-captain must be different |
| Duplicate Players   | No duplicate players allowed               |

## 📂 Project Structure

```text
Fantasy-Cricket-League/
│
├── main.py
│
└── noman_Dugout_league/
    │
    ├── model.py
    ├── rules.py
    ├── loader.py
    │
    └── dugout_starter/
        │
        └── data/
            ├── players.csv
            ├── sample_teams.csv
            └── my_team.csv
```

### File Description

| File               | Responsibility                                        |
| ------------------ | ----------------------------------------------------- |
| `main.py`          | Runs the application and displays league information  |
| `model.py`         | Defines Player, FantasyTeamLeague, and League classes |
| `rules.py`         | Contains fantasy team validation rules                |
| `loader.py`        | Loads player and team data from CSV files             |
| `players.csv`      | Contains the available cricket players                |
| `sample_teams.csv` | Contains sample fantasy teams                         |
| `my_team.csv`      | Contains personally created fantasy teams             |

## 🛠️ Technologies Used

- Object-Oriented Programming (OOP)
- Python CSV Module
- Dictionaries and Lists
- Functions and Methods
- List Comprehensions
- Lambda Functions
- Sorting and Iteration

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Fantasy-Cricket-League.git
```

**2. Navigate to the project directory**

```bash
cd Fantasy-Cricket-League
```

**3. Run the application**

```bash
python main.py
```

No external Python packages are required. The project uses Python's built-in modules.

## 📊 Dataset Information

The project uses CSV files to store player and team information.

**Player CSV columns:**

```text
player_id, name, role, franchise, credits
```

**Team CSV columns:**

```text
team_name, owner, captain, vice_captain, players
```

The `players` column contains semicolon-separated player IDs.

Example:

```text
P122;P089;P056;P075;P039;P065;P012;P068;P114;P101;P015
```

## 🧠 Python Concepts Practiced

This project provides practical experience with:

- Classes and Objects
- Constructors (`__init__`)
- Class Methods (`@classmethod`)
- Encapsulation and Object Relationships
- Dictionaries and Lists
- CSV File Handling
- List Comprehensions
- Lambda Functions
- Sorting with `sorted()`
- Iteration with `for` loops
- Modular Programming
- Data Validation
- Exception Handling

## 🎯 Project Objective

The main objective of this project is to strengthen Python programming skills by developing a structured application that solves a real-world problem.

Instead of writing everything in a single file, the project separates models, business rules, and data-loading operations into different modules.

This makes the application easier to understand, maintain, test, and expand.

## 👨‍💻 Author

**Noman Mehmood**

GitHub: [Noman553](https://github.com/Noman553)

---

*Built with Python 🐍 and a passion for learning software development.*
