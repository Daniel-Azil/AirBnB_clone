#!/usr/bin/python3
"""
    A module that is used in testing the functionality
    of the console.
"""
from unittest.mock import patch
import console
import test
import unittest
import json
import os
from io import StringIO
from models.engine.file_storage import FileStorage
from models.review import Review
from models.user import User
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity


class Test_HBNBConsole(unittest.TestCase):
    """
        A class that is used to test the console
        of HBNBCommand.
    """

    def test_noLines(self):
        """Method test case for empty lines"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("\n")
            self.assertEqual(strIOformat.getvalue(), "")

    def test_documentations(self):
        """Method test case for DocStrings"""
        commandClass = console.HBNBCommand()
        self.assertTrue(len(self.__doc__) >= 1)
        self.assertTrue(len(console.__doc__) >= 1)

    def test_commandCount(self):
        """Method test case for count"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("State.count()")
            self.assertEqual(int, type(eval(strIOformat.getvalue())))

    def test_commandCreate(self):
        """Method test case for create command"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("create Qqqqq")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())

    def test_cmdddestroy(self):
        """Method test case for destroy command"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("destroy QQQQWWWW")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("destroy Review")
            self.assertEqual("** instance id missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("destroy User r934r83hfff")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("BaseModel.destroy('f5g77g')")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("create Review")
            commandClass.onecmd("create Review")

        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("Review.all()")
            self.assertEqual("[[Review]",
                             strIOformat.getvalue()[:9])

    def test_commandAll(self):
        """Method test case for all command"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("all QqqqFfff")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("all BaseModel")
            self.assertEqual("[]\n", strIOformat.getvalue())

    def test_commandShow(self):
        """Method test case for show command"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("test.show()")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("Place.show('f5g77g')")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())

    def test_cmdupdate(self):
        """Method test case upate command"""
        commandClass = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("update QQQFFFF")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("update Review")
            self.assertEqual("** instance id missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            commandClass.onecmd("update Review r934r83hfff")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())


if __name__ == "__main__":
    unittest.main()
