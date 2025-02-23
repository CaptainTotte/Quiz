from fastapi import FastAPI, Request, HTTPException, Depends, status, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Basic authentication for admin panel
security = HTTPBasic()

# Admin credentials (replace with a proper database in production)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Load the JSON file
def load_questions():
    if os.path.exists("questions.json"):
        with open("questions.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return {"categories": [], "questions": {}}

# Save the JSON file
def save_questions(data):
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Convert YouTube URL to embed URL
def convert_to_embed_url(url):
    if "youtu.be" in url:
        video_id = url.split("/")[-1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    elif "youtube.com" in url:
        video_id = url.split("v=")[1].split("&")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# Authentication dependency
def authenticate_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != ADMIN_USERNAME or credentials.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Serve index.html
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

# Serve admin.html
@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request, username: str = Depends(authenticate_admin)):
    data = load_questions()
    flash_message = request.cookies.get("flash_message", None)
    response = templates.TemplateResponse("admin.html", {"request": request, "data": data, "flash_message": flash_message})
    response.set_cookie(key="flash_message", value="", max_age=0)
    return response

# Endpoint to update questions
@app.post("/admin/update")
async def update_questions(
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
    if type == "video":
        content = convert_to_embed_url(content)
    question = next((q for q in data["questions"][points] if q["category"] == category), None)
    if question:
        question["type"] = type
        question["content"] = content
    else:
        data["questions"][points].append({"category": category, "type": type, "content": content})
    save_questions(data)
    response = RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="flash_message", value="Frågan har uppdaterats!")
    return response

# Endpoint to delete a question
@app.post("/admin/delete")
async def delete_question(
    category: str = Form(...),
    points: str = Form(...),
    username: str = Depends(authenticate_admin),
):
    data = load_questions()
    if points in data["questions"]:
        data["questions"][points] = [q for q in data["questions"][points] if q["category"] != category]
        save_questions(data)
    return RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)

# Endpoint to update categories
@app.post("/admin/update_category")
async def update_category(
    current_category: str = Form(...),
    new_category: str = Form(...),
    username: str = Depends(authenticate_admin),
):
    data = load_questions()
    if current_category in data["categories"]:
        data["categories"] = [new_category if cat == current_category else cat for cat in data["categories"]]
        for points in data["questions"]:
            for question in data["questions"][points]:
                if question["category"] == current_category:
                    question["category"] = new_category
        save_questions(data)
        response = RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(key="flash_message", value=f"Kategori '{current_category}' har uppdaterats till '{new_category}'.")
        return response
    else:
        raise HTTPException(status_code=400, detail="Kategorin finns inte.")

# Existing endpoints
@app.get("/categories")
async def get_categories():
    data = load_questions()
    return {"categories": data["categories"]}

@app.get("/questions/{points}")
async def get_questions(points: str):
    data = load_questions()
    if points not in data["questions"]:
        raise HTTPException(status_code=404, detail="Points not found")
    return {"questions": data["questions"][points]}
