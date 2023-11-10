#!/usr/bin/python3
"""Create Custom Console for HBNB project"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Custom console to be used for the HBNB task
    performs custom commands of create, read, update
    and delete
    """
    prompt = '(hbnb) '
    __class = ['BaseModel']

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

    def do_create(self, line):
        """create instance of a class and saves it as json"""
        arg = self.parseline(line)[0]
        if arg is None:
            print("** class name missing **")
        elif arg and arg not in self.__class:
            print("** class doesn't exist **")
        else:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
