# Tambola-Game-with-computer
🎮 Number Match Game – Player vs Computer

A simple Python console-based number matching game where a real player competes against the computer.

The game generates 10 random numbers.
Both the player and the computer have 10 unique numbers.
Numbers are called one by one.
If all 10 numbers of a player are matched, they win.

📌 Features

1 Human Player vs 1 Computer

User manually selects 10 numbers

Computer auto-generates 10 numbers

Random generation of 10 game numbers

Number calling system (one by one)

Automatic marking of matched numbers

Winner detection logic

Draw condition supported

Input validation included

🛠️ Technologies Used

Python 3

random module

Console-based interface

🎯 Game Rules

The user enters 10 unique numbers between 1 and 50.

The computer automatically generates 10 unique random numbers.

The system generates 10 random game numbers.

Numbers are called one by one.

If a called number exists in a player's list, it is marked.

If all 10 numbers of a player are matched → that player wins.

If both match all 10 → it is a draw.

If none match all 10 → no winner.

▶️ How to Run
Step 1: Clone the Repository
git clone https://github.com/your-username/number-match-game.git

Step 2: Navigate to the Project Folder
cd number-match-game

Step 3: Run the Program
python game.py


(Replace game.py with your actual file name if different.)

🧠 Example Gameplay
Enter your 10 unique numbers (between 1 and 50):
Enter number 1: 5
Enter number 2: 12
...

Number Called: 5
You marked 5
Computer marked 5

Your matched count: 1/10
Computer matched count: 1/10

📂 Project Structure
number-match-game/
│
├── game.py
└── README.md

🔍 Concepts Used

Sets for fast number lookup

Random number generation

Input validation

Conditional logic

Loop control structures

🚀 Future Improvements

GUI version using Tkinter

Multiplayer mode

Score tracking system

Replay feature

Sound effects

Web-based version

📜 License

This project is open-source and available under the MIT License.
