from todo import TodoList, Task


class Shell:
    """Runs the shell."""
    def __init__(self):
        self.todolist = TodoList()
        self.commands = {'add': self.todolist.add, 'do': self.todolist.do}

    def print_welcome_message(self):
        """Display simple usage and how many
        messages are currently in the list, if any."""
        msg1 = "Welcome to TODO-app!\n"
        msg2 = "Add entry:\nadd <message>\n"
        msg3 = "Mark as completed:\ndo <number of completed message>\n"
        msg4 = "Display all entries:\nprint\n\n"
        msg5 = f"You currently have {len(self.todolist)} entries.\n"
        print(msg1 + msg2 + msg3 + msg4 + msg5)

    def run(self):
        """Run the shell loop until we get 'exit'."""
        self.print_welcome_message()
        res = ""
        while res != "exit":
            res = input(" > ")
            if res != "exit":
                self.run_command(res)

    def run_command(self, input_str: str):
        if input_str == "test":
            print("This is a response!")


if __name__ == "__main__":
    shell = Shell()
    shell.run()
