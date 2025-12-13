# Masterblog API

A full-stack blog application with a Python Flask backend and a modern web frontend.

## Features

### Backend (Flask)
- RESTful API endpoints for blog post management
- JSON file-based data persistence
- Full CRUD operations (Create, Read, Update, Delete)
- Search and filter functionality
- Sort by title or content
- Input validation and error handling
- CORS support
- Swagger/OpenAPI documentation

### Frontend
- Responsive design
- Real-time post listing
- Create, edit, and delete posts
- Search functionality
- Sort posts by title or content
- Clean and intuitive user interface

## Prerequisites

- Python 3.8+
- Flask
- Flask-CORS
- A modern web browser

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/anastasiafoth/Masterblog-API.git](https://github.com/anastasiafoth/Masterblog-API.git)
   cd Masterblog-API
   
2. Set up a virtual environment and activate it:
   ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
3. Install backend dependencies:
    ```bash
   cd backend
    pip install flask flask-cors
   
4. Start the backend server:
     ```bash
   python backend_app.py
   
5. In a new terminal, install frontend dependencies:
    ```bash
    cd ../frontend
    pip install flask
    
6. Start the frontend server:
    ```bash
    python frontend_app.py
   
7. Open your browser and navigate to:
   ```bash
    http://localhost:5000

### API Documentation
The API documentation is available at:
```bash
    http://localhost:5002/api/docs
```
### API Endpoints
- GET /api/posts - Get all posts (supports sorting with ?sort=title&direction=asc)
- POST /api/posts - Create a new post
- GET /api/posts/search?title=...&content=... - Search posts
- PUT /api/posts/<id> - Update a post
- DELETE /api/posts/<id> - Delete a post
### Project Structure
   ```bash
      Masterblog-API/
      ├── backend/
      │   ├── data/
      │   │   └── posts.json        # Blog post data storage
      │   ├── static/               # Static files
      │   │   └── masterblog.json   # API documentation
      │   └── backend_app.py        # Main Flask application
      │
      └── frontend/
          ├── static/
          │   └── main.js           # Frontend JavaScript
          ├── templates/
          │   └── index.html        # Main HTML template
          └── frontend_app.py       # Frontend server
```
### Usage
1. Viewing Posts
- All posts are displayed on the main page
- Use the sort dropdown to sort by title or content
- Use the search boxes to filter posts
2. Adding a Post
- Fill in the title and content
- Click "Add Post"
3. Editing a Post
- Click the edit button on a post
- Make your changes
- Click "Update"
4. Deleting a Post
- Click the delete button on a post
- Confirm the deletion

### Contributing
1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

### License
This project is licensed under the MIT License - see the LICENSE file for details.

