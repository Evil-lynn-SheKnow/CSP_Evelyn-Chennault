#Evelyn Chennault, Time Notes Python
print("Hello! I am a program will greet you and tell you the time.")
import time

#Current time in seconds
current = time.time()
#Current date and time like normal
now = time.ctime(current)
#Just get a part of time
local_time = time.localtime(current)
hour = local_time.tm_hour #military time (0-23)

if hour == 6 or hour == 7 or hour == 8 or hour == 9 or hour == 10 or hour == 11:
    print("Good morning!")
elif hour == 12 or hour == 13 or hour == 14 or hour == 15 or hour == 16:
    print("Good afternoon!")
elif hour == 17 or hour == 18 or hour == 19 or hour == 20 or hour == 21 or hour == 22:
    print("Good evening!")
elif hour == 23 or hour == 0 or hour == 1 or hour == 2 or hour == 3 or hour == 4 or hour == 5:
    print("Good night!")
