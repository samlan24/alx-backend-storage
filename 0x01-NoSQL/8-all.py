#!/usr/bin/env python3

"""Python function that lists all documents in a collection"""

import pymongo


def list_all(mongo_collection):
    """lists all in a collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
