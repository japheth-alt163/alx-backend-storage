#!/usr/bin/env python3

"""
Python function to insert a new document
in a collection based on kwargs.
"""

from typing import Any
import pymongo


def insert_school(mongo_collection: pymongo.collection.Collection, **kwargs: Any) -> Any:
    """
    Inserts a new document into the specified collection based on keyword arguments.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the fields of the document to be inserted.

    Returns:
        The new _id of the inserted document.
    """
    # Insert document with provided kwargs
    result = mongo_collection.insert_one(kwargs)
    
    return result.inserted_id


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.my_db
    collection = db.school
    new_school_id = insert_school(collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))
