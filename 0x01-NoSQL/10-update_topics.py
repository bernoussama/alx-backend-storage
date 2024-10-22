#!/usr/bin/env python3


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a collection's document with given name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
