from unittest import TestCase
from todo import Task, TodoList


class Test_TodoList(TestCase):
    def test_first_list_is_empty(self):
        """A new TodoList should not have any tasks."""
        new = TodoList()
        self.assertEqual(new.next_id, 0)
        self.assertEqual(new.tasks, list())


class Test_Task(TestCase):
    def test_new_task_must_have_positive_ID(self):
        """A new task must have a positive ID."""
        self.assertRaises(ValueError, lambda: Task("New message.", -1))

    def test_task_must_have_content(self):
        """A new task must have content."""
        self.assertRaises(ValueError, lambda: Task(None, 1))

    def test_new_task_is_uncompleted(self):
        """A new task is uncompleted."""
        new = Task("New message", 1)
        self.assertFalse(new.completed)
