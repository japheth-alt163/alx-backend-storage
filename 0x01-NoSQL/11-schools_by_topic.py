#!/usr/bin/env python3

"""
Python function to return the list of schools having a specific topic.
"""

from typing import List
import pymongo


def schools_by_topic(mongo_collection: pymongo.collection.Collection, topic: str) -> List[dict]:
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic: The topic to search for.

    Returns:
        A list of dictionaries representing schools with the specified topic.
    """
    # Search for schools by topic
    filter_query = {"topics": {"$in": [topic]}}
    schools = list(mongo_collection.find(filter_query))
    
    return schools

if __name__ == "__main__":
    import sys
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.my_db
    collection = db.school
    schools = schools_by_topic(collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
