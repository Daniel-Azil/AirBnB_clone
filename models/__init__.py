#!/usr/bin/python3
"""Initialize the storage module for easy access."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
