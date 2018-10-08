from unittest import TestCase
from todo import Task, TodoList


class Test_TodoList(TestCase):
    ...


class Test_Task(TestCase):
    def test_new_task_must_have_positive_ID(self):
        """A new task must have a positive ID."""
        new = Task("New message")
        self.assertGreaterEqual(new.id, 1, "New message does not have positive ID.")

    def test_task_must_have_content(self):
        """A new task must have content."""
        self.assertRaises(ValueError, lambda: Task(None))
