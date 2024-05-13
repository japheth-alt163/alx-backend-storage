#!/usr/bin/env python3

"""
Python function to change all topics of a school document based on the name.
"""

from typing import List
import pymongo


def update_topics(mongo_collection: pymongo.collection.Collection, name: str, topics: List[str]) -> None:
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object.
        name: The school name to update.
        topics: The list of topics approached in the school.
    """
    # Update topics based on school name
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter_query, update_query)


if __name__ == "__main__":
    import sys
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.my_db
    collection = db.school
    update_topics(collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])
