#!/usr/bin/env python3
"""Return all students sorted by average score."""
from pymongo import MongoClient

def top_students(mongo_collection):
    """Calculate and sort students by average score."""
    pipeline = [
        {
            "$addFields": {
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
