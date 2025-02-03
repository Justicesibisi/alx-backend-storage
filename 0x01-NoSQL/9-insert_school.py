#!/usr/bin/env python3
"""Insert a new document into a collection."""
def insert_school(mongo_collection, **kwargs):
    """Insert a document and return its ID."""
    return mongo_collection.insert_one(kwargs).inserted_id

