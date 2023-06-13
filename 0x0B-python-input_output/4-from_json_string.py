#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def to_json_string(my_obj):
    """
    A function that returns an object (
    Python data structure) represented by a JSON string
    """
    return json.dumps(my_obj)
