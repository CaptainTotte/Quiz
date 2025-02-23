# Jeopardy-Inspired Quiz Game

Welcome to the Jeopardy-Inspired Quiz Game! This project is a web-based quiz game inspired by the popular TV show Jeopardy. Players can select categories and point values to answer questions, and the game includes features like a reset button, an admin panel for managing questions, and interactive animations.

## Features

- **Interactive Game Board**: Players can click on categories and point values to reveal questions.
- **Question Types**: Supports text, image, video, and audio questions.
- **Admin Panel**: Allows admins to add, update, and delete questions.
- **Animations**: Smooth animations for question transitions and button effects.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - [FastAPI](https://fastapi.tiangolo.com/) (for serving static files and handling API requests)
- **Backend**:
  - Python (FastAPI)
- **Data Storage**:
  - JSON file (`questions.json`) for storing questions and categories.

## How to Clone and Run

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CaptainTotte/Quiz.git
   cd Quiz
   ```

### Run with Docker Compose

1. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Access the application in your browser:
   - Open `http://localhost:8000` to play the game.
   - Open `http://localhost:8000/admin` to access the admin panel (username: `admin`, password: `password`).

---

Enjoy playing and managing your Jeopardy-inspired quiz game! 🎉
