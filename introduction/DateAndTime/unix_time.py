#!/usr/bin/python3

""" Notes:

epoch - An instant in time chosen as the origin of a particular
era. Christian epoch starts from day 0 onthe day Jesus was born.

The unix epoch is one of the most popular. This is the time
00:00:00 UTC on 1 January 1970. The date and time in a computer
is determined according to the number of seconds or clock ticks
that have elapsed since the defined epoch for that computer or
platform.

Unix time is the number of seconds elapsed since Unix epoch.

This example prints the unix time and converts it back to
the QDateTime.
"""

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch()
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))
