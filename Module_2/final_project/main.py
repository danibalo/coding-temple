"""
main.py - Module 2 Project entry point
Run this file to execute your pipeline
Once you have implemented DataPipeline in pipeline.py 
Once you have implemented DataPipeline in pipeline.py, running:
python main.py
should load, clean, analyze, visualize, and export the data - all without errors.
"""
import os
from pipeline import DataPipeline
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "messy_employee_survey.csv")
def main():
    print("=" * 60)
    print("Employee Survey Data Pipeline")
    print("=" * 60)
    pipeline = DataPipeline(DATA_PATH)
    results = pipeline.run()
    print("\nPipeline Summary")
    print("-" * 60)
    headcount = results["headcount_by_location"]
    if not headcount.empty:
        print("Top location by headcount: "
              f"{headcount.idxmax()} ({headcount.max()} employees)")
        correlation = results["experience_salary_correlation"]
        print(f"Experience-salary correlation: {correlation:.3f}")
        print("Pipeline completed successfully")
        
if __name__ == "__main__":
    main()
