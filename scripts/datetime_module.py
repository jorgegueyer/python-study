import datetime #date,time,datetime
import pytz

dir(datetime)
dir(datetime.datetime)
print(datetime.datetime.now())
print(datetime.datetime.today())

ist = pytz.timezone('Europe/Madrid')
print(datetime.datetime.now(ist))

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

#print(datetime.datetime.strftime("%y-%m-%d"))
print(datetime.datetime.now().strftime("%Y-%m-%d"))

print(datetime.datetime.now().strftime("%c"))

print(datetime.datetime.fromtimestamp(15555555555))

req_timez = pytz.timezone("Asia/Kolkata")
print(datetime.datetime.now(req_timez))

# strftime("") # strftime.org
from datetime import datetime
print(datetime.now())
