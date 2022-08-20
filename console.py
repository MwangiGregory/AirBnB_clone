#!/usr/bin/python3
"""This module defines a custom cmd class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines an airbnb website clone command line
    intepreter"""
    prompt = '(hbnb)'

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
