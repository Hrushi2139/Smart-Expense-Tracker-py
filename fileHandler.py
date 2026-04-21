import json
import os

File_name="expenditure.json"

def initialize_file():
    if not os.path.exists(File_name):
        with open(File_name,"w") as file:
            json.dump([],file)
