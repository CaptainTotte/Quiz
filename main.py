from fastapi import FastAPI, HTTPException, Depends, status, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
import json
import os
import re

app = FastAPI()

# Mount the static folder to serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates for the admin panel
templates = Jinja2Templates(directory="templates")

# Basic authentication for admin panel
security = HTTPBasic()

# Admin credentials (replace with a proper database in production)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Load the JSON file
def load_questions():
    if os.path.exists("questions.json"):
        with open("questions.json", "r") as file:
            return json.load(file)
    return {"categories": [], "questions": {}}

# Save the JSON file
def save_questions(data):
    with open("questions.json", "w") as file:
        json.dump(data, file, indent=4)

# Convert YouTube URL to embed URL
def convert_to_embed_url(url):
    # Match regular YouTube URL (e.g., https://youtu.be/sxTNACldK3Y)
    if "youtu.be" in url:
        video_id = url.split("/")[-1].split("?")[0]  # Extract video ID
        return f"https://www.youtube.com/embed/{video_id}"
    # Match full YouTube URL (e.g., https://www.youtube.com/watch?v=sxTNACldK3Y)
    elif "youtube.com" in url:
        video_id = url.split("v=")[1].split("&")[0]  # Extract video ID
        return f"https://www.youtube.com/embed/{video_id}"
    return url  # Return the original URL if it's not a YouTube URL

# Authentication dependency
def authenticate_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != ADMIN_USERNAME or credentials.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Endpoint to serve the admin panel
@app.get("/admin", response_class=HTMLResponse)
def admin_panel(request: Request, username: str = Depends(authenticate_admin)):
    data = load_questions()
    # Check for a flash message in cookies
    flash_message = request.cookies.get("flash_message", None)
    response = templates.TemplateResponse("admin.html", {"request": request, "data": data, "flash_message": flash_message})
    # Clear the flash message after displaying it
    response.set_cookie(key="flash_message", value="", max_age=0)
    return response

# Endpoint to update questions
@app.post("/admin/update")
def update_questions(
    category: str = Form(...),
    points: str = Form(...),
    type: str = Form(...),
    content: str = Form(...),
    username: str = Depends(authenticate_admin),
):
    data = load_questions()
    if category not in data["categories"]:
        data["categories"].append(category)
    if points not in data["questions"]:
        data["questions"][points] = []
    # Convert YouTube URL to embed URL if type is video
    if type == "video":
        content = convert_to_embed_url(content)
    # Update or add the question
    question = next((q for q in data["questions"][points] if q["category"] == category), None)
    if question:
        question["type"] = type
        question["content"] = content
    else:
        data["questions"][points].append({"category": category, "type": type, "content": content})
    save_questions(data)
    # Set a flash message in cookies
    response = RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="flash_message", value="Frågan har uppdaterats!")
    return response

# Endpoint to delete a question
@app.post("/admin/delete")
def delete_question(
    category: str = Form(...),
    points: str = Form(...),
    username: str = Depends(authenticate_admin),
):
    data = load_questions()
    if points in data["questions"]:
        data["questions"][points] = [q for q in data["questions"][points] if q["category"] != category]
        save_questions(data)
    return RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)

# Existing endpoints
@app.get("/categories")
def get_categories():
    data = load_questions()
    return {"categories": data["categories"]}

@app.get("/questions/{points}")
def get_questions(points: str):
    data = load_questions()
    if points not in data["questions"]:
        raise HTTPException(status_code=404, detail="Points not found")
    return {"questions": data["questions"][points]}

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html") as f:
        return f.read()