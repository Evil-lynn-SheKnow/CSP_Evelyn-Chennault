#Evelyn Chennault, Time Notes Python
print("Hello! I am a program will tell you the time.")
import time

#Current time in seconds
current = time.time()
#Current date and time like normal
now = time.ctime(current)
#Just get a part of time
local_time = time.localtime(current)
hour = local_time.tm_hour #military time (0-23)

if hour == 4 or hour == 5:
    print("No votes for you yet.\n")
elif hour == 6:
    print("Worry about other things right now. Just be a kid, kid.\n")
elif hour == 12 :
    print("You are not mature enough. In a few years, yes, but not now.\n")

print(hour)