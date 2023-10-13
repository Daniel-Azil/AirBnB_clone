#!/usr/bin/python3

"""
    A module that implements the command line functionality
    of the console Application for the Airbnb.
"""

import cmd
from models.base_model import BaseModel
from models import storage

def seperate_arg(arg):
    """ A custom function that splits given arguments"""
    return tuple(arg.split())

class HBNBCommand(cmd.Cmd):
    """
        A class that inherits from 'Cmd' as the parent
        class
    """

    prompt = '(hbnb)'
    __names_of_class = {"BaseModel"}

    def do_quit(self, cmd_arg):
        """
            A method that exits the commandline program
        """
        return True

    def do_EOF(self, cmd_arg):
        """
            A method that implements 'End of File' for the
            programme execution process.
        """
        return True

    def emptyline(self):
        """
            A method that implements nothing when the enter
            key is pressed with no argument.
        """
        pass

    def do_create(self, cmd_arg):
        """
            A custom method that creats a new class object
            and saves it to JSON file.
        """
        if not cmd_arg or len(cmd_arg) == 0:
            print('** class name missing **')
        elif cmd_arg not in HBNBCommand.__names_of_class:
            print("** class doesn't exist **")
        else:
            created_object = eval(cmd_arg)()
            created_object.save()
            print(created_object.id)

    def do_show(self, class_name_id):
        """
            A custom method that displays the details of given
            classes based on the names and id passed as 
            arguments.
        """
        name_id = seperate_arg(class_name_id)
        if not name_id or len(name_id) == 0:
            print("** class name missing **")
            return
        elif name_id[0] not in HBNBCommand.__names_of_class:
            print("** class doesn't exist **")
            return
        try:
            if name_id[1]:
                storage_saves = "{}.{}".format(name_id[0], name_id[1])
                if storage_saves not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[storage_saves])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, cmd_arg):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(cmd_arg) == 0:
            print("** class name missing **")
            return
        parsed_content = seperate_arg(cmd_arg)
        if parsed_content[0] not in HBNBCommand.__names_of_class:
            print("** class doesn't exist **")
            return
        try:
            if parsed_content[1]:
                saved_content = "{}.{}".format(parsed_content[0], parsed_content[1])
                if saved_content not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[saved_content]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, cmd_arg):
        """ A custom method that displays all the properties
            of all save instances or object created
            but not the class name itself.
        """
        class_name = seperate_arg(cmd_arg)
        stacked_list = []
        if len(cmd_arg) == 0:
            for i in storage.all().values():
                stacked_list.append(i)
            print(stacked_list)
        elif class_name[0] in HBNBCommand.__names_of_class:
            for i, a in storage.all().items():
                if class_name[0] in i:
                    stacked_list.append(a)
            print(stacked_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, cmd_arg):
        """
        A custom method that updates existing instances or
        objects with their IDs as the command cmd_arg argument
        and as well as updating their attributes and save the
        updates or changes into a JSON file.
        """
        cmd_args = seperate_arg(cmd_arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
            return
        if cmd_args[0] not in HBNBCommand.__names_of_class:
            print("** class doesn't exist **")
            return
        if len(cmd_args) == 1:
            print("** instance id missing **")
            return
        instance_id = "{}.{}".format(cmd_args[0], cmd_args[1])
        if instance_id not in storage.all().keys():
            print("** no instance found **")
            return
        if len(cmd_args) == 2:
            print("** attribute name missing **")
            return
        if len(cmd_args) == 3:
            print("** value missing **")
            return

        key = cmd_args[2]
        value = cmd_args[3].strip('\'"')
        obj = storage.all()[instance_id]
        setattr(obj, key, value)
        storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
