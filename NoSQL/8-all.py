#!/usr/bin/env python3
"""8-all: List all documents in a collection"""

def list_all(mongo_collection):
    """
    Returns a list of all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.

    Returns:
        list: List of documents, or empty list if none found.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
