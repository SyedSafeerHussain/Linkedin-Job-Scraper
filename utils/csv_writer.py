import os
import csv
def save_to_csv(jobs,file_path):
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    with open(file_path, mode='w',newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "location",])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)