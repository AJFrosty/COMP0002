from StopWatch import StopWatch
import time as t

start = float(input("Enter an integer to start the program: "))

if start > -1:
    begin = t.time()
    end = float(input("Enter an integer to stop the program: "))
    if end > -1:
        stopped = t.time()
        time = StopWatch(begin, stopped)

print(f"Start time is: {time.getStartTime()} \nEnd time is: {time.getEndTime()} \nElapsed Time: {int(time.getElapsedTime())} ms")