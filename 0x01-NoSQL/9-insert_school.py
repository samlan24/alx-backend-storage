#!/usr/bin/env python3

""" Python function that inserts a new document"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new doc"""
    return mongo_collection.insert_one(kwargs).inserted_id
