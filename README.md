# Hangman-Game
🔤 Hangman Game using Python &amp; MySQL A terminal-based Hangman game built with Python, featuring a classic word-guessing experience. It integrates with MySQL to store and retrieve user scores and game history, making the gameplay more personalized and persistent across sessions.
🚀 Features
Classic word-guessing gameplay in the terminal

User-friendly interface with dynamic feedback

Score tracking and game history storage using MySQL

Supports multiple game sessions per user

Modular and clean codebase for easy customization

🛠️ Tech Stack
Python: Core game logic and user interface

MySQL: Backend database to store scores and history

mysql-connector-python: For connecting Python to MySQL

📦 How to Run
Clone this repository.

Set up the MySQL database using the provided SQL script.

Install dependencies:

bash
Copy
Edit
pip install mysql-connector-python
Run the game:
bash
Copy
Edit
python hangman.py
📁 Folder Structure
pgsql
Copy
Edit
hangman-game/
├── hangman.py
├── db_config.py
├── scores.sql
└── README.md
