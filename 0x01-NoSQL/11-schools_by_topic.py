#!/usr/bin/env python3

"""
Python function that returns the list of school
having a specific topic
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns list of school"""
    return mongo_collection.find({"topics": topic})
