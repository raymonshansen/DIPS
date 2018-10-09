from todo import TodoList, Persister


class Shell:
    """Runs the shell."""
    def __init__(self):
        self.persister = Persister('tasks')
        self.todolist = TodoList(self.persister)
        self.commands = {'add': self.todolist.add,
                         'do': self.todolist.do,
                         'print': self.todolist.print_all_tasks}

    def print_welcome_message(self):
        """Display simple usage and how many
        messages are currently in the list, if any."""
        welcome_message = f"""Welcome to TODO-app!
Add entry:
add <message>
Mark as completed:
do <number of completed message>
Display all entries:
print
You currently have {len(self.todolist)} entries."""
        print(welcome_message)

    def run(self):
        """Run the shell loop until we get 'exit'."""
        self.print_welcome_message()
        res = ""
        while res != "exit":
            res = input(" > ")
            if res and res != "exit":
                self.run_command(res)

    def run_command(self, input_str: str):
        cmd, *args = input_str.split()
        ret_string = self.commands.get(cmd, self.print_default_error)(" ".join(args))
        print(ret_string)

    def print_default_error(self, *args):
        return "Error, unknown command."


if __name__ == "__main__":
    shell = Shell()
    shell.run()
