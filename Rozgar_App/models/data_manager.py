import json
import os
from models.worker import Worker

class DataManager:
    def __init__(self, file_path='data/workers.json'):
        self.file_path = file_path

        # ✅ Create 'data' folder if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        # ✅ Create the workers.json file with [] if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def add_worker(self, worker: Worker):
        data = self.get_all_workers()
        data.append(worker.to_dict())
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all_workers(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def search_workers(self, city=None, skill=None):
        workers = self.get_all_workers()
        if city:
            workers = [w for w in workers if w["city"].lower() == city.lower()]
        if skill:
            workers = [w for w in workers if w["skill"].lower() == skill.lower()]
        return workers
