import json
import os

File_name="expenditure.json"

def initialize_file():
    if not os.path.exists(File_name):
        with open(File_name,"w") as file:
            json.dump([],file)


def load_data():
    with open(File_name,"r") as File:
        return json.load(File)

def save_data(data):
    with open(File_name,"w") as file1:
        json.dump(data,file1,indent=3)
