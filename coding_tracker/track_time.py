#! /usr/bin/env python

import click
import sqlite3

def format_seconds(input_seconds: int):
    seconds = int(input_seconds % 60)
    minutes = int(input_seconds / 60)
    hours = int(input_seconds / 3600)
    return("{hours}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds))

conn = sqlite3.connect('/home/mango/python/coding_tracker/coding_tracker/timer.db')
cursor = conn.cursor()
cursor.execute(f'select * from timer order by timestamp asc')
a = cursor.fetchall()

end = -1
total = 0
for (timestamp, duration) in a:
    timestamp = int(timestamp)
    duration = int(duration)
    if end == -1:
        end = timestamp
    else:
        if timestamp > end:
            total += duration
        else:
            total += (duration - (end - timestamp))
        end = timestamp + duration
        
print(format_seconds(total))
conn.close()
