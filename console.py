#!/usr/bin/python3
"""Create Custom Console for HBNB project"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_show(self, line):
        """Display string representation of an instance"""
        arg1 = self.parseline(line)[0]
        arg2 = self.parseline(line)[1]
        if arg1 is None:
            print("** class name missing **")
        elif arg1 not in self.__class:
            print("** class doesn't exist **")
        elif arg2 == "":
            print("** instance id missing **")
        else:
            key = arg1 + '.' + arg2
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, line):
        """delete an instance of a class"""
        arg1 = self.parseline(line)[0]
        arg2 = self.parseline(line)[1]
        if arg1 is None:
            print("** class name missing **")
        elif arg1 not in self.__class:
            print("** class doesn't exist **")
        elif arg2 == "":
            print("** instance id is missing **")
        else:
            key = arg1 + '.' + arg2
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
