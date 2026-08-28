import time
from datetime import datetime, timezone
import pytest
from src.model import Task


def test_task_initialization_default_status():
    """Test creating a Task with default status."""
    task = Task(id=1, description="Buy groceries")

    assert task.id == 1
    assert task.description == "Buy groceries"
    assert task.status == "todo"
    
    # Check that timestamps are datetime objects in UTC
    assert isinstance(task.createdAt, datetime)
    assert isinstance(task.updatedAt, datetime)
    assert task.createdAt.tzinfo == timezone.utc
    assert task.updatedAt.tzinfo == timezone.utc


def test_task_initialization_custom_status():
    """Test creating a Task with a custom valid status."""
    task = Task(id=2, description="Read book", status="in-progress")

    assert task.id == 2
    assert task.description == "Read book"
    assert task.status == "in-progress"


def test_change_id():
    """Test changing the task ID updates ID and updatedAt timestamp."""
    task = Task(id=1, description="Sample task")
    initial_created_at = task.createdAt
    initial_updated_at = task.updatedAt

    time.sleep(0.001)  # Ensure a slight delay to detect timestamp change
    task.change_id(99)

    assert task.id == 99
    assert task.createdAt == initial_created_at  # createdAt must not change
    assert task.updatedAt > initial_updated_at   # updatedAt must be updated


def test_change_description():
    """Test changing description updates description and updatedAt timestamp."""
    task = Task(id=1, description="Old description")
    initial_created_at = task.createdAt
    initial_updated_at = task.updatedAt

    time.sleep(0.001)
    task.change_description("New description")

    assert task.description == "New description"
    assert task.createdAt == initial_created_at
    assert task.updatedAt > initial_updated_at


@pytest.mark.parametrize("valid_status", ["todo", "in-progress", "done"])
def test_change_status_valid(valid_status):
    """Test updating to all allowed statuses."""
    task = Task(id=1, description="Sample task", status="todo")
    initial_updated_at = task.updatedAt

    time.sleep(0.001)
    task.change_status(valid_status)

    assert task.status == valid_status
    assert task.updatedAt > initial_updated_at


@pytest.mark.parametrize("invalid_status", ["finished", "cancelled", "", None, 123])
def test_change_status_invalid(invalid_status):
    """Test that invalid statuses are ignored and updatedAt is not changed."""
    task = Task(id=1, description="Sample task", status="todo")
    initial_updated_at = task.updatedAt

    time.sleep(0.001)
    task.change_status(invalid_status)

    # Status and updatedAt should remain unchanged
    assert task.status == "todo"
    assert task.updatedAt == initial_updated_at