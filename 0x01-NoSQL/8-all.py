#!/usr/bin/env python3

"""
Script to list all databases in MongoDB.
"""


import pymongo


def list_databases():
    """
    Connects to MongoDB and lists all databases.
    """
    # Connect to MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # List all databases
    databases = client.list_database_names()
    # Print each database name
    for db in databases:
        print(db)


if __name__ == "__main__":
    list_databases()
