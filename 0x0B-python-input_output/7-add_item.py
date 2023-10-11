#!/usr/bin/python3
""" A module that contains one function to read / write list of
command line arguments
"""
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_args = sys.argv
list_data = []

try:
    list_data = load_from_json_file("add_item.json")
except json.JSONDecodeError:
    save_to_json_file(list_data, "add_item.json")
else:
    list_data = load_from_json_file("add_item.json")
    list_data.extend(list_args[1:])
    save_to_json_file(list_data, "add_item.json")
