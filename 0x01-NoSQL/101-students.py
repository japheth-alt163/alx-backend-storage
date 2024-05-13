#!/usr/bin/env python3
"""
students
"""


def top_students(mongo_collection):
    """ 
    Returns all students sorted by average score.
    
    Args:
        mongo_collection: pymongo collection object representing the students collection.
        
    Returns:
        A MongoDB aggregation cursor containing documents representing
        students sorted by average score in descending order.
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
