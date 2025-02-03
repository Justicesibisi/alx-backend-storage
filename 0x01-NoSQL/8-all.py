#!/usr/bin/env python3
"""List all documents in a collection."""
def list_all(mongo_collection):
    """Return list of all documents in a collection."""
    return list(mongo_collection.find()) if mongo_collection.count_documents({}) else[]
