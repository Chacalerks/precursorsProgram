from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client['precursores']  # Replace 'your_database_name' with your actual database name

    def get_collection(self, collection_name):
        return self.db[collection_name]
    
    def insert_labs(self, labs):
        self.get_collection('Labs').insert_many(labs)
    
    def insert_monthly_report(self, report):
        self.get_collection('month_report').insert_one(report)
    
    def find_reports_by_month_year(self, month, year):
        """ Fetch reports for a specific month and year formatted as 'YYYY-MM' """
        collection = self.get_collection('month_report')  # Assuming your collection is named 'monthly_reports'
        return list(collection.find({"month": month, "year": year}, {"_id": 0, "instance": 1}))

def read_labs():
    with open('labs.csv', 'r') as file:
        for line in file:
            labs = []
            for lab in line.split(';'):
                labs.append({'lab': lab.strip()})
            mongo_db.insert_labs(labs)

# Example usage:
if __name__ == "__main__":
    mongo_db = MongoDB()

    
