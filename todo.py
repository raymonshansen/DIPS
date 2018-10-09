from json import load, dump


class Persister:
    """Load and save to disk."""
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        """Load a tasklist from disk."""
        tasks = list()
        next_id = 1
        try:
            with open(self.filename, 'r') as storage:
                temp_list = load(storage)
                for d in temp_list:
                    new = Task(d['text'], d['id'])
                    new.completed = d['completed']
                    tasks.append(new)
                next_id = tasks[-1].id + 1
        except IOError:
            pass

        return tasks, next_id

    def save_tasks(self, tasks):
        """Save current state to disk."""
        with open(self.filename, 'w') as outfile:
            dump([t.to_dict() for t in tasks], outfile)


class TodoList:
    """Represents all current task. Writes to disk or reads them if
    old ones are present."""
    def __init__(self, persister):
        """Construct the Todo-list, either from an existing file,
        or from scratch if no file is found."""
        self.persister = persister
        self.tasks, self.next_id = self.persister.load_tasks()

    def __len__(self):
        """Return the number of current entries."""
        return len(self.tasks)

    def add(self, message: str):
        """Add the message to the list of tasks.
        Returns the string to be printed in the console."""
        ret_string = f"#{self.next_id} {message}"
        self.tasks.append(Task(message, self.next_id))
        self.next_id += 1
        self.persister.save_tasks(self.tasks)
        return ret_string

    def remove_task(self, task):
        """Remove the given task from tasks."""
        self.tasks.remove(task)

    def do(self, id_num: str):
        """Mark the task with the corresponding id_num
        as completed. Try to convert to int, theow error if not.
        Return the string to be printed in the console."""
        if not self.tasks:
            return "No entries to do yet."
        ret_string = f"Error: ID {id_num} not found."
        try:
            num = int(id_num)
            for task in self.tasks:
                if task.id == num:
                    ret_string = f"Completed #{task.id} {task.text}"
                    self.remove_task(task)
                    self.persister.save_tasks(self.tasks)
        except ValueError:
            ret_string = "Error: ID must be number."
        return ret_string

    def print_all_tasks(self, _):
        """Return the string of all current entries."""
        ret_str = "\n".join(f"#{task.id} {task.text}" for task in self.tasks)
        if ret_str:
            return ret_str
        return "No entries yet."


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
        dictionary = {'text': self.text,
                      'id': self.id,
                      'completed': self.completed}
        return dictionary
