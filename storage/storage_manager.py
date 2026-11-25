import json

class StorageManager:
    def __init__(self):
     self.file_name =  "storage/habits.json"

    def save(self, habits):
       with open(self.file_name, "w" ) as file:
          json.dump(habits, file)
    def load(self):
       with open(self.file_name, "r") as file:
          return json.load(file)