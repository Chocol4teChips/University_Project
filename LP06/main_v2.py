import json
from datetime import datetime # datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S

persondict = {
    "fname":"",
    "lname":"",
    "age":0,
    "body_temp":"",
    "location":"",
    "risk":False,
    "covid":True
}

def get_person_info():
