#!/usr/bin/env python3
"""
filter schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school with a specific topic"""
    topic_filter = {
        "topics": {
            "$elemMatch": {
                "$eq": topic,
            },
        },
    }
    return [document for document in mongo_collection.find(topic_filter)]
