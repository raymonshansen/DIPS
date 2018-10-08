from json import load, dump


class TodoList:
    """Represents all current task. Writes to disk or reads them if
    old ones are present."""
    def __init__(self):
        """Construct the Todo-list, either from an existing file,
        or from scratch if no file is found."""
        self.tasks, self.next_id = self.load_tasks()

    def __len__(self):
        """Return the number of current entries."""
        return len(self.tasks)

    def load_tasks(self):
        tasks = list()
        next_id = 1
        try:
            with open('tasks', 'r') as storage:
                temp_list = load(storage)
                for d in temp_list:
                    new = Task(d['text'], d['id'])
                    new.completed = d['completed']
                    tasks.append(new)
                next_id = tasks[-1].id + 1
        except IOError:
            pass

        return tasks, next_id

    def persist_to_disk(self) -> None:
        """Write to fil on disk."""
        with open('tasks', 'w') as outfile:
            dump([t.to_dict() for t in self.tasks], outfile)

    def add(self, message: str):
        """Add the message to the list of tasks.
        Returns the string to be printed in the console."""
        ret_string = f"{self.next_id} {message}"
        self.tasks.append(Task(message, self.next_id))
        self.next_id += 1
        self.persist_to_disk()
        return ret_string

    def do(self, id_num: int):
        """Mark the task with the corresponding id_num
        as completed. Return the string to be printed in the console."""
        ret_string = f"Error: ID {id_num} not found."
        for task in self.tasks:
            if task.id == id_num:
                ret_string = f"Completed {task.id} {task.text}"
        return ret_string

    def print(self):
        ...


class Task:
    def __init__(self, message: str, id_num: int):
        self.check_input(message, id_num)
        self.text = message
        self.id = id_num
        self.completed = False

    def check_input(self, message, id_num):
        """Raise errors if input is incorrect."""
        if message is None:
            raise ValueError("Cannot make Task without content.")
        if id_num <= 0:
            raise ValueError("Task must have positive ID.")
        if not isinstance(id_num, int):
            raise ValueError("Task ID must be int.")

    def to_dict(self):
        """Return self as a dictionary."""
        dictionary = {'text': self.text, 'id': self.id, 'completed': self.completed}
        return dictionary
