# Jeopardy-Inspired Quiz Game

Welcome to the Jeopardy-Inspired Quiz Game! This project is a web-based quiz game inspired by the popular TV show Jeopardy. Players can select categories and point values to answer questions, and the game includes features like a reset button, an admin panel for managing questions, and interactive animations.

## Disclaimer

This application is designed for temporary or local use during events or livestreams. As such, robust security measures—such as secure username/password management and proper database integration—have not been implemented. It is intended for event-specific use only.

## Features

- **Interactive Game Board**: Players can click on categories and point values to reveal questions.
- **Question Types**: Supports text, image, video, and audio questions. All by external URL's.
- **Admin Panel**: Allows admins to add, update, and delete questions & categories.
- **Animations**: Smooth animations for question transitions and button effects.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - [FastAPI](https://fastapi.tiangolo.com/) (for serving static files and handling API requests)
- **Backend**:
  - Python (FastAPI)
- **Data Storage**:
  - JSON file (`questions.json`) for storing questions and categories.

## Images

### Gameboard
![Screenshot 1](https://i.postimg.cc/BQV7D4g4/SCR-20250227-lvdo.png)
### Admin Panel
![Screenshot 2](https://i.postimg.cc/7LvBs9dR/SCR-20250227-lvgp.png)
### Buttons
![Screenshot 3](https://i.postimg.cc/9Qw8YK8T/SCR-20250227-lwlm.png)

## How to Clone and Run

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CaptainTotte/Quiz.git
   cd Quiz
   ```

### Configs

- You will find the admin username and password in main.py if you wish to change it. (Recommended)
- Port is easiest changed within the docker compose file.

### Run with Docker Compose

1. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```   

3. Access the application in your browser:
   - Open `http://localhost:8000` to play the game.
   - To access the admin panel (username: `admin`, password: `password`).

---

Enjoy playing and managing your Jeopardy-inspired quiz game! 🎉
