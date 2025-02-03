#!/usr/bin/env python3
"""Update school topics based on name."""
def update_topics(mongo_collection, name, topics):
    """Update topics for schools with the given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
