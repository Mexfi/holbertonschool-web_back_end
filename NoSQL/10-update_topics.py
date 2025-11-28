#!/usr/bin/env python3
"""10-update_topics: Update the topics of a school document based on its name"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all documents in a MongoDB collection with the given name,
    setting their 'topics' field to the provided list.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        name (str): The name of the school to update.
        topics (list): List of topics to set in the document.

    Returns:
        None
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
