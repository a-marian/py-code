import pytest
from task_manager import TaskManager  # Assuming the class is saved in a file called task_manager.py

@pytest.fixture
def task_manager():
    """Fixture to create a new TaskManager instance for each test."""
    return TaskManager()

def test_add_task(task_manager):
    # Test adding a valid task
    response = task_manager.add_task("Buy groceries")
    assert response == "Task 'Buy groceries' added."
    assert "Buy groceries" in task_manager.list_tasks()

    # Test adding a duplicate task
    response = task_manager.add_task("Buy groceries")
    assert response == "Task already exists."

    # Test adding an empty task
    response = task_manager.add_task("")
    assert response == "Invalid task."

    # Test adding a None task
    response = task_manager.add_task(None)
    assert response == "Invalid task."

def test_remove_task(task_manager):
    # Initially add tasks to the manager
    task_manager.add_task("Read a book")

    # Test removing a valid task
    response = task_manager.remove_task("Read a book")
    assert response == "Task 'Read a book' removed."
    assert "Read a book" not in task_manager.list_tasks()

    # Test removing a non-existent task
    response = task_manager.remove_task("Read a book")
    assert response == "Task not found."

def test_list_tasks(task_manager):
    # Add tasks for listing
    task_manager.add_task("Do laundry")
    task_manager.add_task("Write code")

    # Test listing tasks
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert "Do laundry" in tasks
    assert "Write code" in tasks

def test_empty_list(task_manager):
    # Test listing when no tasks have been added
    tasks = task_manager.list_tasks()
    assert tasks == []
