# 🎮 Hangman Game — Python & Streamlit

A classic **Hangman word-guessing game** built with **Python, Object-Oriented Programming (OOP), and Streamlit**.

The project started as a console-based Python game and was later converted into an interactive web-based application using Streamlit. The main purpose of this project is not only to create a playable game, but also to practice and demonstrate important Python programming concepts such as **classes, objects, encapsulation, composition, inheritance, abstraction, modular design, and state management**.

---

## 📌 Project Overview

Hangman is a word-guessing game where the player attempts to discover a hidden word by guessing one letter at a time.

For every correct guess, the player earns points. Incorrect guesses reduce the number of remaining attempts and affect the player's score.

The game contains words from different categories, allowing the player to choose a topic before starting.

### 🎯 Main Features

* 👤 Player name input
* 📚 Multiple word categories
* 🎲 Random word selection
* 🔤 Letter-by-letter guessing
* ❤️ Limited number of attempts
* 🏆 Score system
* ❌ Wrong guess tracking
* 🔁 Repeated-letter detection
* 🎨 Interactive Streamlit interface
* 🧱 Object-Oriented architecture
* 🧩 Factory-based game creation
* 💾 Streamlit session state for maintaining the game
* 📊 Real-time game information

---

## 🛠️ Technologies Used

| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| 🐍 Python              | Core programming language |
| 🎨 Streamlit           | Web-based user interface  |
| 🧱 OOP                 | Project architecture      |
| 🎲 Random              | Random word selection     |
| 📦 Virtual Environment | Dependency isolation      |
| 🔗 Git & GitHub        | Version control           |

---

# 🏗️ Project Architecture

The project is divided into multiple classes and modules.

This separation keeps the code organized and allows each class to have a specific responsibility.

### Project Structure

```text
Hangman Game Python/
│
├── frontend.py
├── connector.py
├── HangmanGame.py
├── player.py
├── word.py
├── score.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📂 File Descriptions

### `frontend.py`

This file contains the **Streamlit user interface**.

It is responsible for:

* Displaying the game interface
* Getting the player's name
* Allowing category selection
* Starting the game
* Displaying the current game state
* Accepting letter guesses
* Showing attempts
* Showing the player's score
* Displaying game messages

The frontend communicates with the game objects rather than implementing the actual game rules itself.

---

### `connector.py`

The connector acts as a bridge between the Streamlit interface and the game logic.

It contains the `GameFactory`, which is responsible for creating the required objects and preparing a game.

The idea is to keep the frontend from directly handling the construction of all game components.

For example:

```python
factory = GameFactory(player_name, category)

game = factory.create_game()
```

This makes the application easier to maintain and extend.

---

### `HangmanGame.py`

This module contains the main `Game` class.

The `Game` object coordinates the major components of the application:

```text
Player
   ↓
Game
   ↓
Word
   ↓
Score
```

The game is responsible for things such as:

* Processing guesses
* Checking whether a letter has already been guessed
* Updating the score
* Tracking wrong guesses
* Decreasing attempts
* Checking the game status

---

### `player.py`

Contains the `Player` class.

The player object stores information related to the person playing the game.

Example responsibilities:

```text
Player
 ├── player_name
 └── guessed_letters
```

The class provides functionality for:

* Storing the player's name
* Recording guessed letters
* Checking whether a letter was already guessed

---

### `word.py`

Contains the `Word` class.

The class is responsible for the hidden word and operations related to it.

Example responsibilities:

* Checking whether a letter exists in the word
* Displaying guessed letters
* Checking whether the complete word has been discovered

For example, if the secret word is:

```text
python
```

and the player has guessed:

```text
p
t
o
```

the game might display:

```text
p _ t _ o _
```

---

### `score.py`

Contains the `Score` class.

The score system manages the player's points.

Correct guesses increase the score, while incorrect guesses decrease it.

Example:

```text
Correct Guess → +10 points
Wrong Guess   → -5 points
```

The score is encapsulated inside the `Score` object so that it can be controlled through class methods and properties.

---

# 📚 Word Categories

The game currently contains several categories.

### 💻 Programming & Architecture

Example words:

```text
python
streamlit
fastapi
assembly
emulator
register
memory
```

### 🗄️ Databases & Networking

Example words:

```text
postgres
database
schema
coalesce
topology
router
subnet
```

### 📈 Marketing & E-Commerce

Example words:

```text
klaviyo
copywriting
commerce
sequence
retention
metric
```

### 🧠 Logic & Science

Example words:

```text
physics
algorithm
variable
function
interface
```

### 🎌 Anime & Animation

Example words:

```text
naruto
uzumaki
madara
goku
kamado
```

---

# 🎮 How the Game Works

## 1️⃣ Enter Your Name

The player starts by entering their name.

Example:

```text
Enter your name: Sami
```

---

## 2️⃣ Select a Category

The player chooses the category from the available options.

For example:

```text
Programming & Architecture
```

---

## 3️⃣ Start the Game

After clicking the **Start Game** button, the application creates a new game.

The game factory creates the necessary objects:

```text
Player
Word
Score
Game
```

---

## 4️⃣ Guess a Letter

The player enters a letter.

For example:

```text
Guess: p
```

The game checks whether the letter exists in the secret word.

---

## 5️⃣ Correct Guess

If the letter exists:

```text
Correct guess!
```

The player's score increases.

Example:

```text
Score: +10
```

The guessed letter is also revealed.

---

## 6️⃣ Incorrect Guess

If the letter does not exist:

```text
Wrong guess!
```

The player loses points and one attempt.

Example:

```text
Score: -5
Attempts remaining: 5
```

---

## 7️⃣ Repeated Guess

If the player enters a letter that has already been guessed, the game detects it.

For example:

```text
You already guessed this letter.
```

The game does not process the same guess again.

---

## 8️⃣ Winning the Game

The player wins when all letters in the hidden word have been discovered.

Example:

```text
Secret Word:

python

Player guesses:

p → correct
y → correct
t → correct
h → correct
o → correct
n → correct
```

The game then displays a winning message.

---

## 9️⃣ Losing the Game

The player loses when all available attempts are used.

For example:

```text
Attempts remaining: 0
```

The game ends and the secret word can be revealed.

---

# 🧱 Object-Oriented Programming Concepts

One of the main purposes of this project is practicing **Object-Oriented Programming**.

The project uses several OOP concepts.

## 🔹 Encapsulation

Different pieces of data are managed inside their respective classes.

For example, the score belongs to the `Score` class instead of being directly manipulated throughout the application.

```python
class Score:

    def __init__(self):
        self.__score = 0
```

The private attribute:

```python
__score
```

helps control how the score is accessed and modified.

---

## 🔹 Composition

The `Game` class works with objects created from other classes.

Conceptually:

```text
Game
 ├── Player
 ├── Word
 └── Score
```

Instead of putting everything inside one large class, responsibilities are divided among multiple objects.

---

## 🔹 Abstraction

The project separates the details of game logic from the user interface.

The Streamlit frontend does not need to know every internal detail of how a guess is processed.

It can simply interact with the game object.

For example:

```python
result = game.process_guess(letter)
```

The game internally handles the required logic.

---

## 🔹 Modular Programming

The project is divided into separate Python files.

Instead of having one huge file:

```text
frontend.py
```

the project separates responsibilities:

```text
player.py
word.py
score.py
HangmanGame.py
connector.py
frontend.py
```

This makes the project easier to understand, debug, and maintain.

---

# 🔄 Game Flow

The overall application flow can be represented as:

```text
                ┌───────────────┐
                │     Start     │
                └───────┬───────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Enter Player Name│
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Select Category  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   GameFactory    │
              └────────┬─────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │      Create Game        │
          └────────────┬────────────┘
                       │
                       ▼
             ┌───────────────────┐
             │   Guess a Letter  │
             └─────────┬─────────┘
                       │
                 ┌─────┴─────┐
                 │           │
              Correct      Wrong
                 │           │
                 ▼           ▼
              +10 Score    -5 Score
                 │           │
                 └─────┬─────┘
                       │
                       ▼
              ┌───────────────────┐
              │ Attempts Remaining│
              └─────────┬─────────┘
                        │
                        ▼
               Continue Playing
                        │
                        ▼
                  Win / Lose
```

---

# 💾 Streamlit Session State

Because Streamlit reruns the Python script whenever the user interacts with the application, the project uses `st.session_state` to preserve the current game.

For example:

```python
if "game" not in st.session_state:
    st.session_state.game = None
```

When the game is created:

```python
st.session_state.game = factory.create_game()
```

The game object can then remain available between interactions.

This is important because without session state, the application could recreate or lose the current game whenever the user interacts with the interface.

---

# ▶️ Installation

## Prerequisites

Make sure you have:

* Python 3.x
* Git
* A GitHub account
* Basic knowledge of Python

---

## 1. Clone the Repository

Clone the repository using Git:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Then move into the project directory:

```bash
cd "Hangman Game Python"
```

---

## 2. Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

For Git Bash, you can use:

```bash
source .venv/Scripts/activate
```

---

## 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Streamlit manually:

```bash
pip install streamlit
```

---

# 🚀 Running the Application

Start the Streamlit application using:

```bash
streamlit run frontend.py
```

Streamlit will start a local development server.

You can then open the application in your browser.

---

# 🖥️ User Interface

The application provides an interactive interface where the player can:

```text
┌─────────────────────────────────┐
│       🎮 HANGMAN GAME           │
├─────────────────────────────────┤
│                                 │
│  Player Name: Sami              │
│                                 │
│  Category: Programming          │
│                                 │
│  Word: p _ t _ o _               │
│                                 │
│  Attempts: ❤️❤️❤️❤️❤️           │
│                                 │
│  Score: 40                      │
│                                 │
│  Guess a letter: [ ___ ]        │
│                                 │
│           [ Guess ]              │
│                                 │
└─────────────────────────────────┘
```

---

# 🎯 Learning Objectives

This project was created as a practical way to strengthen Python programming skills.

Through this project, the following concepts are practiced:

* Python classes
* Objects
* Constructors
* `self`
* Encapsulation
* Private attributes
* Properties
* Composition
* Modular programming
* Object interaction
* Random selection
* Lists
* Strings
* Conditional statements
* Loops
* Exception/error handling
* Streamlit
* `st.session_state`
* Basic application architecture
* Git
* GitHub
* Virtual environments

---

# 🔮 Future Improvements

Possible improvements for future versions include:

### 🎨 Better UI

* Add Hangman graphics
* Improve the overall layout
* Add animations
* Add custom themes
* Improve mobile responsiveness

### 🏆 Leaderboard

Add a leaderboard that stores:

```text
Player Name
Score
Category
Words Completed
Games Played
```

### 📊 Statistics

Track player statistics such as:

```text
Total Games
Games Won
Games Lost
Highest Score
Average Score
```

### 🌎 More Categories

Additional categories could include:

```text
Movies
Sports
Countries
Technology
Programming Languages
History
Science
Geography
```

### 🔐 User Accounts

A future version could include authentication so that players can create accounts and maintain their own statistics.

### 🗄️ Database Integration

The project could eventually use a database such as PostgreSQL or SQLite to store:

* Players
* Scores
* Game history
* Categories
* Words
* Leaderboards

---

# 🧪 Example Game

Suppose the player chooses:

```text
Category: Programming & Architecture
```

The randomly selected word is:

```text
streamlit
```

The player initially sees:

```text
_ _ _ _ _ _ _ _ _
```

The player guesses:

```text
s
```

Result:

```text
s _ _ _ _ _ _ _ _
```

Then:

```text
t
```

Result:

```text
s t _ _ _ _ _ _ t
```

A wrong guess such as:

```text
z
```

results in:

```text
Wrong Guess!
Attempts Remaining: 5
```

The player continues until either:

```text
🎉 Word Completed
```

or:

```text
💀 No Attempts Remaining
```

---

# 📁 Git Workflow

This project can also be used to practice Git and GitHub.

### Check project status

```bash
git status
```

### Add changes

```bash
git add .
```

### Commit changes

```bash
git commit -m "Update Hangman game"
```

### Push changes

```bash
git push
```

### Pull latest changes

```bash
git pull
```

---

# 🔐 Using SSH with GitHub

This project can be cloned and managed through GitHub using SSH.

After configuring an SSH key, you can clone the repository using the SSH repository URL:

```bash
git clone git@github.com:USERNAME/REPOSITORY.git
```

You can test your GitHub SSH connection with:

```bash
ssh -T git@github.com
```

A successful connection should confirm that GitHub has authenticated your SSH key.

---

# 🤝 Contributing

Contributions and improvements are welcome.

If you want to contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add new feature"
```

5. Push your branch

```bash
git push origin feature/new-feature
```

6. Open a Pull Request

---

# 🐛 Bug Reports

If you find a bug, feel free to open an issue.

When reporting a bug, try to include:

* What you were doing
* What you expected to happen
* What actually happened
* The error message
* Relevant screenshots
* Python version
* Operating system

This makes it easier to reproduce and fix the problem.

---

# 📜 License

This project is created for **learning and educational purposes**.

You are free to study the code and use the concepts demonstrated in this project.

---

# 👨‍💻 Author

**Muhammad Sami**

This project was built as part of my journey to strengthen my **Python programming, Object-Oriented Programming, and application development skills**.

---

# ⭐ If You Like This Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Thanks for checking out the project! 🎮🐍
