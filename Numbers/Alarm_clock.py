#Play a sound at a certain time or after a certian period of time
import pyglet
import time
import sys
import calendar
decision = raw_input("Do you want to set alarm afer a certain period of time (1) or want to specify the time of alarm (2)?    ")

def play_alarm(alarm, current):
    while current < alarm:
        time.sleep(1)
        current_time = time.time()
        print "{0} seconds to alarm".format(int(alarm_time-current_time))
    print "ALARM !!!"
    music = pyglet.resource.media('test.mp3')
    music.play()
    pyglet.app.run()
    sys.exit(0)

while True:
    if decision == "1":
        try:        
            passed = int(raw_input("Specify the time after which the alarm should sound in seconds:> "))
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
        current_time = time.time()
        alarm_time = current_time + passed
        play_alarm(alarm_time, current_time)   
    elif decision == "2":
        entry = raw_input("Please enter the time in the form h:m in 24 hour format, example 14:27  ")
        entry2 = entry.split(":")
        a = time.localtime()
        alarm_time = []
        for i in range(0, len(a)):
            alarm_time.append(a[i])
        alarm_time[3] = int(entry2[0])
        alarm_time[4] = int(entry2[1])
        b = calendar.timegm(alarm_time) - 7200 # Because of the summer time
        current_time = time.time()
        play_alarm(b, current_time)
    else:
        decision = raw_input("Please enter 1 - period of time or 2") 
a = time.time()
print a

