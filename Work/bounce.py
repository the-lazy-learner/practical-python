#!/usr/bin/env python3
# bounce.py
#
# Exercise 1.5

height = 100 # in metres
times_bounced = 0

while times_bounced <= 10:
    times_bounced = times_bounced + 1
    height = 3 / 5 * height
    print(times_bounced, round(height, 4))
