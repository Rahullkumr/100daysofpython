# USA States Game

This is an interactive Python game where users attempt to name all 50 U.S. states. The program will show an image of the United States and ask users to input state names. If a correct state name is entered, it will be displayed on the map. The game also generates a file with the names of any states the player missed.

## Features
- Displays a map of the USA with a blank outline of the states.
- Allows users to guess states' names and shows correct guesses on the map.
- Generates a `states_you_missed.csv` file listing any states not guessed during the game.

## Prerequisites
1. **Python 3.x**: Ensure Python is installed. You can download it from [Python.org](https://www.python.org/).
2. **Pandas**: Install the `pandas` library for data manipulation:
   ```
   pip install pandas
   ```
3. **Turtle Graphics**: The `turtle` module is a standard Python library, so no additional installation is needed.

## Project Structure
- `main.py`: Main game file containing the code to run the game.
- `50_states.csv`: CSV file with state names and their coordinates.
- `blank_states_img.gif`: Image of the USA map outline used as the game background.

## Getting Started

1. **Clone the repository**: Clone the project to your local machine using Git.
   ```
   git clone <repository-url>
   ```

2. **Navigate to the project directory**:
   ```
   cd <project-directory>
   ```

3. **Ensure all required files are in the directory**:
   - `main.py`
   - `50_states.csv`
   - `blank_states_img.gif`

## Running the Game

To start the game, execute the following command:
```
python main.py
```

## How to Play

1. When the game starts, a prompt will appear asking for a state name.
2. Type the name of a state and press Enter.
3. If the state name is correct, it will appear on the map at the state's location.
4. Type "Exit" if you want to stop the game early.
   - When you exit, a `states_you_missed.csv` file will be created in the project directory, listing any states you did not guess.

## Note

- Ensure that `blank_states_img.gif` is present in the same directory as the code. If it's missing, the game will not display the background map.

## Author
- Created by [Rahul Kumar](https://github.com/rahullkumr)

Enjoy learning and challenging yourself with this USA states guessing game!
