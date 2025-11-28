#!/usr/bin/env python3
"""12-log_stats: Provides stats about Nginx logs in MongoDB"""

from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of documents
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Number of documents per HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET /status requests
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()
