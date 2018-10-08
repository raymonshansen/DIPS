from unittest import TestCase, main as test_main
from todo import Task, TodoList


class Test_TodoList(TestCase):
    def test_first_list_is_empty(self):
        """A new TodoList should not have any tasks."""
        new = TodoList()
        self.assertEqual(new.next_id, 0)
        self.assertEqual(new.tasks, list())

    def test_TodoList_adds_single_message(self):
        """A new message gets added to the list of tasks."""
        todolist = TodoList()
        ret_string = "1 New message"
        self.assertEqual(todolist.add("New message"), ret_string)

    def test_TodoList_completes_message(self):
        todolist = TodoList()
        ret_string = "Completed 1 New message"
        self.assertEqual(todolist.do(1), ret_string)

    def test_TodoList_has_correct_length(self):
        """Make sure __len__ is implemented."""
        todolist = TodoList()
        todolist.add("New message")
        self.assertEqual(len(todolist), 1)


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

    def test_task_can_convert_self_to_dictionary(self):
        """A task can return itself as a dictionary."""
        new = Task("New message", 1)
        dict_str = new.to_dict()
        compare = {"text": "New message", "id": 1, "completed": False}
        self.assertEqual(dict_str, compare)


if __name__ == '__main__':
    test_main()
