#!/usr/bin/python3
"""Create Custom Console for HBNB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Custom console to be used for the HBNB task
    performs custom commands of create, read, update
    and delete
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handle end of file input"""
        print("")
        return True

    def do_quit(self, line):
        """close or quit from console"""
        return True

    def emptyline(self):
        """handle when no input + ENTER is hit"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
