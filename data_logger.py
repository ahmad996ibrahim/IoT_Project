import json
import random
import time
import os
from datetime import datetime

current_path =(os.path.dirname(__file__))
os.chdir(current_path)
current_folder= os.getcwd()

logger_folder = os.path.join(current_folder , "buffer_folder")

if not os.path.exists(logger_folder) :
    os.makedirs(logger_folder)
    print("buffer folder has created sucessfuly")

def kuka_robot_arm ():
    return{
        "joint_temp1" : random.uniform(20.0 , 70.0),
        "motor_current" : random.uniform(10.0 , 20.0),
        "status" : "Running"
        }
historical_data = []
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
fileName = f"Kuka_log_{timestamp}.json"
filepath= os.path.join(logger_folder , fileName)
for i in range(5):
    raw_data = kuka_robot_arm()
    payload = {
        "meta_data" : {
            "factory_id" : "Dubai_001",
            "machine_ID" : "kuka_27000",
            "timestamp" : datetime.now().isoformat()
        },
        "robot_data" : {
            "tempbycelesuis" : round(raw_data["joint_temp1"],2),
            "currentbyAmp" : round(raw_data["motor_current"],2),
            "status" : raw_data["status"]           
        }
    }
    historical_data.append(payload)
    time.sleep(1)

with open(filepath, "w") as json_file:
    json.dump(historical_data,json_file,indent=4)

print("logger kukua robot arm has sucessfuly buffered")