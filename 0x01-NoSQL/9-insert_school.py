#!/usr/bin/env python3
"""
insert a document
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
