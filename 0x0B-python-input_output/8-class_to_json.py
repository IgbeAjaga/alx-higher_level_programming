#!/usr/bin/python3

def class_to_json(obj):
    """Converts an object to a JSON-serializable dictionary"""
    return obj.__dict__
