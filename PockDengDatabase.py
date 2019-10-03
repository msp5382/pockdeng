import os
import json
def saveRoom(data):
    with open("RoomDatabase.txt", "w") as write_file:
        json.dump(data, write_file)
        

def readRoom():
    with open("RoomDatabase.txt", "r") as read_file:
        data = json.load(read_file)
        return data

def saveJao(data):
    with open("JaoDatabase.txt", "w") as write_file:
        json.dump(data, write_file)
        

def readJao():
    with open("JaoDatabase.txt", "r") as read_file:
        data = json.load(read_file)
        return data

def clearJao():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "WebServ/JaoDatabase.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, "w") as write_file:
        write_file.write('0')