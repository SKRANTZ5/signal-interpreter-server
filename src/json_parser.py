# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:49:39 2024

@author: SKRANTZ5
"""

import json as js
from src.custom_exception import MyCustomError
from src import logger


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        try:
            with open(file_path, "r") as my_file:  # open the json file
                self.data = js.load(my_file)
                logger.info("File data read %s", self.data)
        except FileNotFoundError:
            raise MyCustomError("File not found", 400)

    def get_signal_title(self, identifier):
        for entry in self.data["services"]:  # loop services in self.data
            if entry["id"] == identifier:
                return entry["title"]
        raise MyCustomError("Signal not found", 404)
