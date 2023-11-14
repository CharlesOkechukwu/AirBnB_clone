#!/usr/bin/python3
"""Create Custom Console for HBNB project"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Custom console to be used for the HBNB task
    performs custom commands of create, read, update
    and delete
    """
    prompt = '(hbnb) '
    __class = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

    def do_EOF(self, line):
        """Handle end of file input"""
        print("")
        return True

    def do_quit(self, line):
        """Close or quit from console"""
        return True

    def emptyline(self):
        """Handle when no input + ENTER is hit"""
        pass

    def do_create(self, line):
        """Create instance of a class and saves it as json"""
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
        """Delete an instance of a class"""
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
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Print all instances associated with a class or not"""
        arg1 = self.parseline(line)[0]
        obj_dict = storage.all()
        if arg1 is None:
            print([str(obj_dict[inst]) for inst in obj_dict])
        elif arg1 not in self.__class:
            print("** class doesn't exist **")
        else:
            value = obj_dict.values()
            cls_inst = []
            for inst in value:
                if arg1 == inst.__class__.__name__:
                    cls_inst.append(inst.__str__())
            print(cls_inst)

    def do_update(self, line):
        """Update attributes value in an instance"""
        args = line.split(" ")
        cmd = self.parseline(line)[0]
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                keys = instance.__dict__.keys()
                k_type = None
                if args[2] in keys:
                    k_type = type(instance.__dict__[args[2]])
                if k_type in [int, float, str]:
                    instance.__dict__[args[2]] = k_type(args[3])
                else:
                    instance.__dict__[args[2]] = args[3]
                storage.save()

    def default(self, line):
        """Handles other commands and unknown commands"""

        command_list = line.split(".")
        class_name = command_list[0]
        if class_name in self.__class:
            cmd = command_list[1]
            if cmd == "all()":
                self.do_all(class_name)
            elif cmd == "count()":
                # self.do_count(class_name)
                print("count command not implemented yet")
            else:
                all_commands = ["show", "destroy", "update"]
                basic_cmd = cmd[0:cmd.find('(')]  # show, update
                if basic_cmd in all_commands:
                    if basic_cmd == "show":
                        id = eval(cmd[cmd.find('(') + 1:cmd.find(')')])
                        self.do_show("{} {}\n".format(class_name, id))
                    elif basic_cmd == "destroy":
                        id = eval(cmd[cmd.find('(') + 1:cmd.find(')')])
                        self.do_destroy("{} {}\n".format(class_name, id))
                    elif basic_cmd == "update":
                        id = eval(cmd[cmd.find('(') + 1:cmd.find(')')])
                        if type(id[1]) == dict:
                            for key, value in id[1].items():
                                self.do_update(
                                    "{} {} {} {}".format(
                                        class_name,
                                        id[0],
                                        key,
                                        value
                                        )
                                    )
                        else:
                            self.do_update(
                                "{} {} {} {}".format(
                                    class_name,
                                    id[0],
                                    id[1],
                                    id[2]
                                    )
                                )
                else:
                    print("*** Unknown syntax: {}".format(line))

        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
