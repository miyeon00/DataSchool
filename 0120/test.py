from todo_client import (
    create_todo, read_todo, read_all_todos, 
    update_todo, delete_todo
)

print("=" * 60)
print("MULTI-USER TODO CRUD SERVICE - TEST EXAMPLES")
print("=" * 60)

# --- USER 1: ALICE ---
print("\n[USER: alice]")
print("-" * 60)

print("\n1. CREATE - Alice adding todos")
alice_todo1 = create_todo("alice", "Buy groceries", "Milk, eggs, bread")
print(f"Created: {alice_todo1['title']}")

alice_todo2 = create_todo("alice", "Finish project", "Complete the Python CRUD service")
print(f"Created: {alice_todo2['title']}")

alice_todo3 = create_todo("alice", "Exercise", "30 minutes workout")
print(f"Created: {alice_todo3['title']}")

print("\n2. READ ALL - Alice's todos")
alice_todos = read_all_todos("alice")
for todo in alice_todos:
    status = "✓" if todo["completed"] else "○"
    print(f"  [{status}] ID {todo['id']}: {todo['title']}")

print("\n3. UPDATE - Alice marks exercise as done")
updated = update_todo("alice", 3, completed=True)
print(f"Marked '{updated['title']}' as completed")

# --- USER 2: BOB ---
print("\n\n[USER: bob]")
print("-" * 60)

print("\n1. CREATE - Bob adding todos")
bob_todo1 = create_todo("bob", "Study Python", "Learn decorators and generators")
print(f"Created: {bob_todo1['title']}")

bob_todo2 = create_todo("bob", "Write report", "Q1 analysis report")
print(f"Created: {bob_todo2['title']}")

print("\n2. READ ALL - Bob's todos")
bob_todos = read_all_todos("bob")
for todo in bob_todos:
    status = "✓" if todo["completed"] else "○"
    print(f"  [{status}] ID {todo['id']}: {todo['title']}")

print("\n3. UPDATE - Bob updates report task")
updated = update_todo("bob", 2, description="Q1 2026 analysis report")
print(f"Updated '{updated['title']}': {updated['description']}")

# --- USER 3: CHARLIE ---
print("\n\n[USER: charlie]")
print("-" * 60)

print("\n1. CREATE - Charlie adding a todo")
charlie_todo1 = create_todo("charlie", "Setup environment", "Install dependencies")
print(f"Created: {charlie_todo1['title']}")

print("\n2. READ ALL - Charlie's todos")
charlie_todos = read_all_todos("charlie")
for todo in charlie_todos:
    status = "✓" if todo["completed"] else "○"
    print(f"  [{status}] ID {todo['id']}: {todo['title']}")

# --- OPERATIONS ACROSS USERS ---
print("\n\n" + "=" * 60)
print("MULTI-USER OPERATIONS")
print("=" * 60)

print("\nAll Users Summary:")
for username in ["alice", "bob", "charlie"]:
    todos = read_all_todos(username)
    completed = sum(1 for t in todos if t["completed"])
    print(f"  {username}: {len(todos)} total, {completed} completed")

# --- DELETE OPERATION ---
print("\n\nDelete - Alice removes a todo")
deleted = delete_todo("alice", 2)
print(f"Deleted todo ID 2 from alice: {deleted}")

print("\nAlice's todos after deletion:")
alice_todos = read_all_todos("alice")
for todo in alice_todos:
    status = "✓" if todo["completed"] else "○"
    print(f"  [{status}] ID {todo['id']}: {todo['title']}")

# --- FINAL STATE ---
print("\n\n" + "=" * 60)
print("FINAL STATE - All Users")
print("=" * 60)
for username in ["alice", "bob", "charlie"]:
    todos = read_all_todos(username)
    print(f"\n{username}:")
    if todos:
        for todo in todos:
            status = "✓" if todo["completed"] else "○"
            print(f"  [{status}] ID {todo['id']}: {todo['title']}")
    else:
        print("  (no todos)")

print("\n" + "=" * 60)
print("All user data saved in 'todos.json' (nested by username)")
print("=" * 60)
