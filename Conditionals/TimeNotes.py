#Evelyn Chennault, Time Notes Python
import time

#First instance of time in prgramming
first_time = time.gmtime()
#print(first_time)

#current time in seconds
current = time.time()
#print(current) #Seconds saince 1/1/1970

#Current date and time like normal
now = time.ctime(current)
#print(now)

#Just get a part of time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour #military time (0-23)
print(hour)