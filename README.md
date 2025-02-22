# Jeopardy-Inspired Quiz Game

Welcome to the Jeopardy-Inspired Quiz Game! This project is a web-based quiz game inspired by the popular TV show Jeopardy. Players can select categories and point values to answer questions, and the game includes features like a reset button, an admin panel for managing questions, and interactive animations.

## Features

- **Interactive Game Board**: Players can click on categories and point values to reveal questions.
- **Question Types**: Supports text, image, video, and audio questions.
- **Admin Panel**: Allows admins to add, update, and delete questions.
- **Responsive Design**: Works on both desktop and mobile devices.
- **Animations**: Smooth animations for question transitions and button effects.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - [FastAPI](https://fastapi.tiangolo.com/) (for serving static files and handling API requests)
- **Backend**:
  - Python (FastAPI)
- **Data Storage**:
  - JSON file (`questions.json`) for storing questions and categories.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/jeopardy-quiz-game.git
   cd jeopardy-quiz-game
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be available at `http://127.0.0.1:8000`.

4. **Access the Game**:
   - Open your browser and navigate to `http://127.0.0.1:8000`.
   - The admin panel can be accessed at `http://127.0.0.1:8000/admin`.

### Docker Setup (Optional)

1. **Build the Docker Image**:
   ```bash
   docker build -t jeopardy-quiz-game .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 8000:8000 jeopardy-quiz-game
   ```

3. **Access the Application**:
   - Open your browser and navigate to `http://localhost:8000`.

## File Structure

```
jeopardy-quiz-game/
├── static/               # Static files (CSS, JS, images, etc.)
│   ├── styles.css        # Main stylesheet
│   ├── script.js         # Main JavaScript file
│   └── admin.css         # Admin panel stylesheet
├── templates/            # HTML templates
│   └── admin.html        # Admin panel template
├── main.py               # FastAPI application
├── questions.json        # JSON file for storing questions
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Admin Panel

The admin panel allows you to manage questions and categories. To access it:

1. Navigate to `http://127.0.0.1:8000/admin`.
2. Use the following credentials:
   - **Username**: `admin`
   - **Password**: `password`

### Adding/Updating Questions

1. Select a category, point value, and question type (text, image, video, or audio).
2. Enter the question content (e.g., text, image URL, video URL, or audio URL).
3. Click "Uppdatera Fråga" to save the question.

### Deleting Questions

1. Select the category and point value of the question you want to delete.
2. Click "Delete" to remove the question.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy playing and managing your Jeopardy-inspired quiz game! 🎉
