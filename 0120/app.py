from flask import Flask, render_template, request, jsonify
from todo_client import (
    create_todo, read_todo, read_all_todos, 
    update_todo, delete_todo, load_all_data
)

app = Flask(__name__)


@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')


# === API ENDPOINTS ===

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all usernames."""
    data = load_all_data()
    users = list(data.keys()) if data else []
    return jsonify({"users": users})


@app.route('/api/todos/<username>', methods=['GET'])
def get_todos(username):
    """Get all todos for a specific user."""
    todos = read_all_todos(username)
    return jsonify({"username": username, "todos": todos})


@app.route('/api/todos/<username>', methods=['POST'])
def create_todo_api(username):
    """Create a new todo for a user."""
    data = request.json
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    try:
        new_todo = create_todo(
            username,
            data['title'],
            data.get('description', '')
        )
        return jsonify(new_todo), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/todos/<username>/<int:todo_id>', methods=['PUT'])
def update_todo_api(username, todo_id):
    """Update a todo for a user."""
    data = request.json
    
    try:
        updated = update_todo(
            username,
            todo_id,
            title=data.get('title'),
            description=data.get('description'),
            completed=data.get('completed')
        )
        
        if updated is None:
            return jsonify({"error": "Todo not found"}), 404
        
        return jsonify(updated), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/todos/<username>/<int:todo_id>', methods=['DELETE'])
def delete_todo_api(username, todo_id):
    """Delete a todo for a user."""
    deleted = delete_todo(username, todo_id)
    
    if not deleted:
        return jsonify({"error": "Todo not found"}), 404
    
    return jsonify({"message": "Todo deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
