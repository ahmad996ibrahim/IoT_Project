import json
import random
import time
from datetime import datetime

def kuka_robot_arm ():
    return{
        "joint_temp1" : random.uniform(20.0 , 70.0),
        "motor_current" : random.uniform(10.0 , 20.0),
        "status" : "Running"
        }

historical_data = []

print("Starting Data Acquisition from KUKA Robot...")

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

print(historical_data)

json_output = json.dumps(historical_data,indent=4)
print("\n--- Final JSON Payload ready for AWS IoT or Machine Learning Pipeline ---")
print(json_output)