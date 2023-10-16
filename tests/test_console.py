#!/usr/bin/python3
"""
    A module that is used in testing the functionality
    of the console.
"""
from unittest.mock import patch 
import tests
import console
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
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("\n")
            self.assertEqual(strIOformat.getvalue(), "")  
  
    @classmethod
    def initialise_instance(self):
        """Method test case initialise an instance"""
        self.commandclass = console.HBNBCommand()
:
    def test_documentations(self):
        """Method test case for DocStrings"""
        self.assertTrue(len(self.__doc__) >= 1)
        self.assertTrue(len(console.__doc__) >= 1)

    def test_commandCount(self):
        """Method test case for count"""
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("State.count()")
            self.assertEqual(int, type(eval(strIOformat.getvalue())))

    def test_commandCreate(self):
        """Method test case for create command"""
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("create Qqqqq")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())

    def test_cmdddestroy(self):
        """Method test case for destroy command"""
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("destroy QQQQWWWW")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("destroy Review")
            self.assertEqual("** instance id missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("destroy User r934r83hfff")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("BaseModel.destroy('f5g77g')")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())  
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("create Review")
            self.commandclass.onecmd("create Review") 

        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("Review.all()")
            self.assertEqual("[[Review]",
                             strIOformat.getvalue()[:9])

    def test_commandAll(self):
        """Method test case for all command"""
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("all QqqqFfff")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("all BaseModel")
            self.assertEqual("[]\n", strIOformat.getvalue())

    def test_commandShow(self):
        """Method test case for show command"""
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("test.show()")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("Place.show('f5g77g')")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())

    def test_cmdupdate(self):
        """Method test case upate command"""
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("update QQQFFFF")
            self.assertEqual("** class doesn't exist **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("update Review")
            self.assertEqual("** instance id missing **\n",
                             strIOformat.getvalue())
        with patch('sys.stdout', new=StringIO()) as strIOformat:
            self.commandclass.onecmd("update Review r934r83hfff")
            self.assertEqual("** no instance found **\n",
                             strIOformat.getvalue())


if __name__ == "__main__":
    unittest.main()
