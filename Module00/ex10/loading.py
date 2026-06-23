#!/usr/bin/env python3
import time

#ETA(Estimated Time of Arrival)
#\r=> each time it return to the same line, for progress bar, ech time after updating return to the same line
#yield => Unlike the return keyword which stops further execution of the function, the yield keyword returns the result so far, and continues to the next step.
#yield returns a value and pauses the function. return returns a value and terminates the function


def ft_progress(lst):
    total = len(lst)
    start = time.time()
    bar_size = 20

    for i, elem in enumerate(lst,1):
        elapsed = time.time() - start
        percent =  int(i / total *100)
        eta = (total - i) * elapsed / i
        filled = int(bar_size * i /total)
        bar = "=" *filled + ">" + " " * (bar_size - filled)
        print(
            f"ETA: {eta:.2f}s [{percent:3d}%]"
            f"[{bar}] {i}/{total} | elapsed time {elapsed:.2f}s",
            end="\r")
        yield elem
"""
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
"""
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)