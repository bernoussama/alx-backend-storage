#!/usr/bin/env python3
"""
filter schools by topic
"""

from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Prints stats about mongo request logs in nginx"""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        req_count = len(list(nginx_collection.find({"method": method})))
        print(f"\tmethod {method}: {req_count}")
    status_checks_count = len(
        list(nginx_collection.find({"method": "GET", "path": "/status"}))
    )
    print(f"{status_checks_count} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx_request_logs(client.logs.nginx)
