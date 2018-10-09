from unittest import TestCase, main as test_main
from todo import Task, TodoList


class MockPersister:
    def __init__(self, tasks):
        self.save_count = 0
        self.load_count = 0
        self.tasks = tasks

    def load_tasks(self):
        self.load_count += 1
        if not self.tasks:
            return list(), 1
        return self.tasks, self.tasks[:-1].id + 1

    def save_tasks(self, tasks):
        self.save_count += 1
        self.tasks = tasks.copy()


class Test_TodoList(TestCase):
    def setUp(self):
        self.mock_persister = MockPersister(list())

    def test_first_TodoList_is_empty(self):
        """A blank TodoList should be empty."""
        new = TodoList(self.mock_persister)
        self.assertEqual(new.next_id, 1)
        self.assertEqual(new.tasks, list())
        self.assertEqual(self.mock_persister.load_count, 1)

    def test_TodoList_adds_single_message(self):
        """A new message gets added to the list of tasks."""
        todolist = TodoList(self.mock_persister)
        ret_string = "#1 New message"
        self.assertEqual(todolist.add("New message"), ret_string)
        actual_task = self.mock_persister.tasks[0]
        self.assertEqual(actual_task.text, "New message")
        self.assertEqual(actual_task.id, 1)

    def test_TodoList_completes_a_message(self):
        """A completed message gets removed."""
        todolist = TodoList(self.mock_persister)
        todolist.add("New message")
        ret_string = "Completed #1 New message"
        self.assertEqual(todolist.do("1"), ret_string)
        self.assertEqual(0, len(self.mock_persister.tasks))

    def test_TodoList_add_then_complete(self):
        todolist = TodoList(self.mock_persister)
        after_add = "#1 New message"
        self.assertEqual(todolist.add("New message"), after_add)
        actual_task = self.mock_persister.tasks[0]
        self.assertEqual(actual_task.text, "New message")
        self.assertEqual(actual_task.id, 1)
        after_do = "Completed #1 New message"
        self.assertEqual(1, len(self.mock_persister.tasks))
        self.assertEqual(todolist.do("1"), after_do)
        self.assertEqual(0, len(self.mock_persister.tasks))

    def test_TodoList_notifies_if_id_does_not_exist(self):
        todolist = TodoList(self.mock_persister)
        todolist.add("New message")
        after_invalid = "Error: ID 404 not found."
        self.assertEqual(todolist.do("404"), after_invalid)

    def test_TodoList_notifies_if_id_is_not_a_number(self):
        todolist = TodoList(self.mock_persister)
        todolist.add("New message")
        after_invalid = "Error: ID must be number."
        self.assertEqual(todolist.do("fem"), after_invalid)

    def test_TodoList_notifies_that_empty_list_cannot_be_completed(self):
        """Notify that nicely that we cannot complete from an empty list."""
        todolist = TodoList(self.mock_persister)
        after_do_empty = "No entries to do yet."
        self.assertEqual(todolist.do("1"), after_do_empty)

    def test_TodoList_cannot_print_empty_list(self):
        """Notify nicely that the todo-list is empty."""
        todolist = TodoList(self.mock_persister)
        after_print = "No entries yet."
        self.assertEqual(todolist.print_all_tasks([]), after_print)

    def test_TodoList_has_correct_length(self):
        """Make sure __len__ is implemented."""
        todolist = TodoList(self.mock_persister)
        todolist.add("One")
        todolist.add("Two")
        todolist.add("Three")
        self.assertEqual(len(todolist), 3)

    def test_TodoList_adds_unique_id_after_several_adds_and_a_do(self):
        """Can add several, one do and still have unique number."""
        todolist = TodoList(self.mock_persister)
        todolist.add("One")
        todolist.add("Two")
        todolist.add("Three")
        todolist.do("2")
        todolist.add("This message should have ID: 4")
        self.assertEqual(todolist.next_id, 5)

    def test_TodoList_can_add_empty_item(self):
        """If we want, we can have empty items."""
        todolist = TodoList(self.mock_persister)
        after_add_empty = "#1 "
        self.assertEqual(todolist.add(""), after_add_empty)
        self.assertEqual(1, len(self.mock_persister.tasks))


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
