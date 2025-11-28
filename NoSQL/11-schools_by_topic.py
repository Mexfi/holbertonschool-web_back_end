#!/usr/bin/env python3
"""11-schools_by_topic: Return schools having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        topic (str): The topic to search for.

    Returns:
        list: List of school documents matching the topic.
    """
    if mongo_collection is None or not topic:
        return []
    return list(mongo_collection.find({ "topics": { "$in": [topic] } }))
