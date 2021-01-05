import json
provinces = {
    "1"  : "กรุงเทพมหานคร",
    "2"  : "จังหวัดกาญจนบุรี",
    "3"  : "จังหวัดจันทบุรี",
    "4"  : "จังหวัดฉะเฉิงเทรา",
    "5"  : "จังหวัดชุมพร",
    "6"  : "จังหวัดชุมพร",
    "7"  : "จังหวัดชลบุรี",
    "8"  : "จังหวัดตราด",
    "9"  : "จังหวัดตาก",
    "10" : "จังหวัดนครนายก",
    "11" : "จังหวัดนครปฐม",
    "12" : "จังหวัดนนทบุรี",
    "13" : "จังหวัดปทุมธานี",
    "14" : "จังหวัดปราจีนบุรี",
    "15" : "จังหวัดพระนครศรีอยุธยา",
    "16" : "จังหวัดเพชรบุรี",
    "17" : "จังหวัดราชบุรี",
    "18" : "จังหวัดระนอง",
    "19" : "จังหวัดระยอง",
    "20" : "จังหวัดลพบุรี",
    "21" : "จังหวัดสิงห์บุรี",
    "22" : "จังหวัดสมุทรปราการ",
    "23" : "จังหวัดสมุทรสงคราม",
    "24" : "จังหวัดสมุทรสาคร",
    "25" : "จังหวัดสุพรรณบุรี",
    "26" : "จังหวัดสระแก้ว",
    "27" : "จังหวัดสระบุรี",
    "28" : "จังหวัดอ่างทอง",
    "0"  : "อื่นๆ"
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
elif str(persondict.get("location")) in provinces.keys() and persondict.get("body_temp") > 37.5 and  persondict.get("body_temp") != 0:
    persondict.update({"covid":True})
elif str(persondict.get("location")) in provinces.keys():
    persondict.update({"risk":True})
if persondict.get("body_temp") > 37.5:
    persondict.update({"risk":True})


x = json.dumps(persondict)
print("{}".format(json.dumps(persondict)))