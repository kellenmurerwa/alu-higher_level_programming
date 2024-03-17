#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and then saves them to a file.
"""

import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if the file exists
filename = "add_item.json"
if path.exists(filename):
    # Load existing data from the file
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Append arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)