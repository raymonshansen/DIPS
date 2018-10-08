from json import load


class TodoList:
    """Represents all current task. Writes to disk or reads them if
    old ones are present."""
    def __init__(self):
        """Construct the Todo-list, either from an existing file,
        or from scratch if no file is found."""
        self.tasks, self.next_id = self.load_tasks()

    def load_tasks(self):
        tasks = list()
        next_id = 0
        try:
            with open('tasks', 'r') as storage:
                temp_list = load(storage)
                for d in temp_list:
                    new = Task(d['text'], d['id'])
                    new.completed = d['completed']
                    tasks.append(new)
                next_id = self.tasks[-1].id + 1
        except IOError:
            pass

        return tasks, next_id

    def persist(self):
        ...


class Task:
    def __init__(self, message: str, id_num: int):
        self.check_input(message, id_num)
        self.text = message
        self.id = id_num
        self.completed = False

    def check_input(self, message, id_num):
        if message is None:
            raise ValueError("Cannot make Task without content.")
        if id_num <= 0:
            raise ValueError("Task must have positive ID.")
        if not isinstance(id_num, int):
            raise ValueError("Task ID must be int.")
