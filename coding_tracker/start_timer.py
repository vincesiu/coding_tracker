#!/usr/bin/env python

import datetime
import subprocess
import sqlite3
import time



handle = subprocess.run("pgrep -t tty1", shell=True, capture_output=True)
if handle.returncode == 0:
    print(handle.stdout.decode("ascii"))
    print(datetime.datetime.now())

    conn = sqlite3.connect('/home/mango/python/coding_tracker/coding_tracker/timer.db')
    conn.execute(f'insert into timer values ({time.time()}, 305)')
    conn.commit()
    conn.close()

    print("successfully added to database")
