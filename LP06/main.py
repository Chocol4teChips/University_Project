import json
from datetime import datetime # datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
provinces = {
    "1"  : "Bangkok",
    "2"  : "Kanchanaburi",
    "3"  : "Chanthanaburi",
    "4"  : "Chachoengsao",
    "5"  : "Chumphone",
    "6"  : "Chonburi",
    "7"  : "trat",
    "8"  : "Tak",
    "9"  : "Nakhon Nayok",
    "10" : "Nakhon Pathom",
    "11" : "Nonthaburi",
    "12" : "Pathum Thani",
    "13" : "Prachuap Khiri Khan",
    "14" : "Prachinburi",
    "15" : "Ayutthaya",
    "16" : "Phetchinburi",
    "17" : "Ratchaburi",
    "18" : "Ranong",
    "19" : "Rayong",
    "20" : "Lopburi",
    "21" : "Singburi",
    "22" : "Samut Prakn",
    "23" : "Samut Songkhram",
    "24" : "Samut Sakhon",
    "25" : "Suphanburi",
    "26" : "Sa Kaeo",
    "27" : "Saraburi",
    "28" : "Ang Thong",
    "0"  : "other"
}

persondict = {
    "date_time" : dt_string,
    "fname" : str(input("Enter first name : ")),
    "lname" : str(input("Enter last name : ")),
    "age" : int(input("Enter Age : ")),
    "body_temp" : float(input("Enter body temperature : ")),
    "location" : "",
    "risk" : False,
    "covid" : False
}
print("Location")
for x,y in provinces.items():
    print("{}.{}".format(x,y))
persondict.update({"location":int(input("Enter location number : "))})

if persondict.get("location") == 0:
    persondict.update({"risk":False})
elif str(persondict.get("location")) in provinces.keys() and persondict.get("body_temp") > 37.5 and  persondict.get("provinces") != 0:
    persondict.update({"covid":True})
elif str(persondict.get("location")) in provinces.keys():
    persondict.update({"risk":True})
if persondict.get("body_temp") > 37.5:
    persondict.update({"risk":True})

x = json.dumps(persondict)
print("{}".format(json.dumps(persondict)))