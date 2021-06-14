from datetime import datetime, timedelta
id_num = input("Please enter your Id: ")
id_number = list(id_num)

print(id_number)

birthyear = id_number[0:2]
birthmonth = id_number[2:4]
birthdate = id_number[4:6]

birthdate = str(birthdate)

print(birthdate.strftime("%y"))
