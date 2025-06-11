

# 🍉 Fruit Ninja Game (Python + Pygame)

This is a **Fruit Ninja-style slicing game** built using **Python** and **Pygame**. The player slices fruits flying across the screen while avoiding bombs. The goal is to score as many points as possible within the time limit. The game also features difficulty levels, high score tracking, sound effects, and a colorful interface.

---

## 🎮 Game Features

* ✅ **Multiple fruit types** with different graphics
* 💣 **Bombs** that end the game if sliced
* 🕹️ **Mouse swipe detection** for slicing action
* 🕒 **Countdown timer** to limit gameplay
* ⭐ **Score tracking** and **high score saving**
* 📈 **Difficulty progression** (levels increase over time)
* 🔊 **Sound effects** (slicing, bomb explosion, game over)
* 🎨 **Colorful visuals** and improved background graphics
* 🔁 **Game over screen** with restart and quit options

---

## 🧠 How It Works

* Fruits and bombs are randomly generated and thrown on the screen at intervals.
* The player uses the mouse to "slice" through the fruits.
* Slicing fruits increases the score. Slicing a bomb ends the game instantly.
* The game increases in difficulty as time passes (more/faster fruits).
* A countdown timer runs in the top corner.
* The highest score is saved in a file and displayed on the game over screen.

---

## 🛠️ Technologies Used

* Python 3.x
* Pygame library

---

## 🚀 How to Run

### Prerequisites:

* Python installed on your system (version 3.6+ recommended)
* Pygame library installed:

  ```bash
  pip install pygame
  ```

### Run the Game:

```bash
python main.py
```

Or, if you’re using PDM or virtual environments:

```bash
pdm run python main.py
```

---

## 📂 Project Structure

```
fruit-ninja/
│
├── main.py                 # Main game logic
├── assets/                 # Images and sounds
│   ├── fruits/             # Fruit images
│   ├── bombs/              # Bomb images
│   └── sounds/             # Slicing, bomb, game over sounds
├── high_score.txt          # Saves the highest score
├── README.md               # Project description
└── requirements.txt        # Dependencies
```
## 📌 To Do / Future Improvements

* Add more fruit types and animations
* Mobile/touch support
* Power-ups or combo bonuses
* Pause/resume feature

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
