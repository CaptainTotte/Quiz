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
   git clone https://github.com/CaptainTotte/Quiz.git
   cd Quiz
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

### Docker Setup

You can run the application using Docker for a containerized deployment.

#### Using Dockerfile

1. **Build the Docker Image**:
   ```bash
   docker build -t quiz .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 8000:8000 quiz
   ```

3. **Access the Application**:
   - Open your browser and navigate to `http://localhost:8000`.

#### Using Docker Compose

1. **Start the Application with Docker Compose**:
   ```bash
   docker-compose up
   ```

2. **Access the Application**:
   - Open your browser and navigate to `http://localhost:8000`.

### Dockerfile

The `Dockerfile` is used to build the Docker image for the application:

```dockerfile
# Use an official Python-based image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port FastAPI runs on (default is 8000)
EXPOSE 8000

# Run the FastAPI application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

The `docker-compose.yaml` file simplifies running the application with Docker:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"  # Map port 8000 on the host to port 8000 in the container
    volumes:
      - .:/app       # Mount the project directory for live updates during development
    environment:
      - APP_ENV=development  # Environment variables (can be customized)
```

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
├── Dockerfile            # Dockerfile for containerized deployment
├── docker-compose.yaml   # Docker Compose configuration
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
