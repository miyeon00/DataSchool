import json
import os
from datetime import datetime
from typing import Optional, List, Dict, Any

TODOS_FILE = "todos.json"

def load_all_data() -> Dict[str, List[Dict[str, Any]]]:
    """Load all users' todos from JSON file. Returns empty dict if file doesn't exist."""
    if not os.path.exists(TODOS_FILE):
        return {}
    
    try:
        with open(TODOS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_all_data(data: Dict[str, List[Dict[str, Any]]]) -> None:
    """Save all users' todos to JSON file."""
    with open(TODOS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_todos(username: str) -> List[Dict[str, Any]]:
    """Load todos for a specific user. Returns empty list if user doesn't exist."""
    data = load_all_data()
    return data.get(username, [])


def save_todos(username: str, todos: List[Dict[str, Any]]) -> None:
    """Save todos for a specific user."""
    data = load_all_data()
    data[username] = todos
    save_all_data(data)


def get_next_id(username: str) -> int:
    """Get the next available todo ID for a user."""
    todos = load_todos(username)
    if not todos:
        return 1
    return max(todo["id"] for todo in todos) + 1


def create_todo(username: str, title: str, description: str = "") -> Dict[str, Any]:
    """Create a new todo for a user and save it."""
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    
    todos = load_todos(username)
    new_todo = {
        "id": get_next_id(username),
        "title": title.strip(),
        "description": description.strip(),
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    
    todos.append(new_todo)
    save_todos(username, todos)
    return new_todo


def read_todo(username: str, todo_id: int) -> Optional[Dict[str, Any]]:
    """Read a single todo by ID for a user."""
    todos = load_todos(username)
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None


def read_all_todos(username: str) -> List[Dict[str, Any]]:
    """Read all todos for a user."""
    return load_todos(username)


def update_todo(username: str, todo_id: int, title: Optional[str] = None, 
                description: Optional[str] = None, 
                completed: Optional[bool] = None) -> Optional[Dict[str, Any]]:
    """Update a todo by ID for a user. Pass only the fields you want to update."""
    todos = load_todos(username)
    
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            if title is not None:
                if not title.strip():
                    raise ValueError("Title cannot be empty")
                todo["title"] = title.strip()
            
            if description is not None:
                todo["description"] = description.strip()
            
            if completed is not None:
                todo["completed"] = completed
            
            todo["updated_at"] = datetime.now().isoformat()
            save_todos(username, todos)
            return todo
    
    return None


def delete_todo(username: str, todo_id: int) -> bool:
    """Delete a todo by ID for a user. Returns True if deleted, False if not found."""
    todos = load_todos(username)
    
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            save_todos(username, todos)
            return True
    
    return False