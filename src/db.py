from pymongo import MongoClient
import os
from dotenv import load_dotenv
import logging
from bson import ObjectId

# Setup logging
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

class MongoDB:
    def __init__(self):
        try:
            self.client = MongoClient(os.getenv('MONGO_URI'),  serverSelectionTimeoutMS=5000)  # Timeout for initial connection
            # Attempt to fetch server info to check if connected successfully
            self.client.server_info()
            self.db = self.client['precursores']  # Replace 'precursores' with your actual database name if different
            logging.info("MongoDB connection established.")
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            raise Exception("Database connection failed.")

    def get_collection(self, collection_name):
        try:
            return self.db[collection_name]
        except Exception as e:
            logging.error(f"Error accessing collection {collection_name}: {e}")
            raise

    def insert_labs(self, labs):
        try:
            self.get_collection('Labs').insert_many(labs)
        except Exception as e:
            logging.error(f"Error inserting labs data: {e}")
            raise

    def insert_monthly_report_by_instance(self, report):
        try:
            self.get_collection('month_report_by_instance').insert_one(report)
            return True
        except Exception as e:
            logging.error(f"Error inserting monthly report: {e}")
            raise
    def insert_monthly_report(self, report):
        try:
            self.get_collection('month_report').insert_one(report)
        except Exception as e:
            logging.error(f"Error inserting monthly report: {e}")
            raise
    def update_monthly_report(self, report):
        try:
            # Extract the _id from the report and convert it to ObjectId
            document_id = ObjectId(report['_id'])
            collection = self.get_collection('month_report')
            # Update the document with new report data, using the _id field
            result = collection.update_one(
                {"_id": document_id},    # Query document using ObjectId
                {"$set": report},        # Update document
                upsert=True              # Insert if not exists (usually not necessary with _id)
            )
            logging.info(f"Modified {result.modified_count} documents, Upserted {result.upserted_id}")
        except Exception as e:
            logging.error(f"Error updating monthly report based on _id: {e}")
            raise

    def find_reports_by_month_instance(self, month, instance):
        try:
            collection = self.get_collection('month_report')
            return list(collection.find({"month": month, "instance": instance}, {"_id": 0}))
        except Exception as e:
            logging.error(f"Error fetching reports for {month} at {instance}: {e}")
            raise
    def get_month_reports_by_instance(self):
        try:
            self.month_report_by_instance = self.get_collection('month_report_by_instance')            
        except Exception as e:
            logging.error(f"Error accessing collection month_reports: {e}")
            raise
    def get_month_reports(self):
        try:
            self.month_report = self.get_collection('month_report')            
        except Exception as e:
            logging.error(f"Error accessing collection month_reports: {e}")
            raise

def read_labs():
    try:
        with open('labs.csv', 'r') as file:
            labs = []
            for line in file:
                for lab in line.split(';'):
                    labs.append({'lab': lab.strip()})
            mongo_db.insert_labs(labs)
    except Exception as e:
        logging.error(f"Error reading labs from file: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    try:
        mongo_db = MongoDB()
        # Additional code to utilize the database connection can go here
    except Exception as e:
        logging.error(f"Application failed: {e}")
