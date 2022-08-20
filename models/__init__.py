#!/usr/bin/python3
"""This module creates a file storage, an
instance of FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
