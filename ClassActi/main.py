info = {
    "fname": "xxxxxxxxxxx",
    "lname": "xxxxxxxxxxx",
    "stdID": "xxxxxxxxxx",
    "age": 19,
    "GPAX": 4.00
}

address = {
    "number":"30",
    "villageNO":"45",
    "sub_Area":"sub_district",
    "district":"district",
    "province":"province",
    "postal_code":"postal_code"
}

student = {
    "student_info" : info,
    "student_address" : address
}
for x,y in student.items():
    print(x,y)