#!/usr/bin/env python3
"""
Provides some stats about Nginx logs including the top 10 most present IPs.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Access the logs database and the nginx collection
    col = client.logs.nginx
    
    # Count the total number of logs
    total_logs = col.estimated_document_count()
    print("{} logs".format(total_logs))
    
    # Count the number of logs for each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = col.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))
    
    # Count the number of logs for each status check
    status_get = col.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(status_get))
    
    # Find the top 10 most present IPs
    print("IPs:")
    top_ips = col.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))
