#!/usr/bin/python3
"""This module defines a custom cmd class"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines an airbnb website clone command line
    intepreter"""
    prompt = '(hbnb)'
    class_list = ['BaseModel']

    def do_create(self, line):
        """create class_name
        creates a new instance of class_name, saves it
        and prints it's id"""
        if not line:
            print("** class name missing **")
        else:
            if line not in self.class_list:
                print("** class doesn't exist **")
            else:
                obj = eval(line + "()")
                models.storage.new(obj)
                models.storage.save()
                print(obj.id)

    def do_show(self, arg):
        """show class_name object_id

        Prints the string representation of an instance
        based on the class name and the instance id"""
        args_list = arg.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif len(args_list) >= 1:
            obj_className = args_list[0]
            if obj_className not in self.class_list:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
                elif len(args_list) >= 2:
                    class_name = args_list[0]
                    obj_id = args_list[1]
                    key = class_name + "." + obj_id
                    dict_objects = models.storage.all()
                    if key in dict_objects:
                        print(str(dict_objects[key]))
                    else:
                        print("** no instance found **")

    def do_destroy(self, line):
        """ destroy class_name instance_id
        Deletes an instance base on the class_name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) >= 1:
            if args[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                elif len(args) >= 2:
                    class_name = args[0]
                    obj_id = args[1]
                    key = class_name + "." + obj_id
                    dict_objects = models.storage.all()
                    if key in dict_objects:
                        models.storage.delete(dict_objects[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
        return False

    def do_EOF(self, arg):
        """Exit the hbnb console"""
        return True

    def do_quit(self, arg):
        """Exit the hbnb console"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered
        as input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
