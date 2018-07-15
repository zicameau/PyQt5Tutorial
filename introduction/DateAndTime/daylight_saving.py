#! /usr/bin/python3

""" This example checks if the datetime is in the daylight
savings time. """

from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()

print("Time zone: {0}".format(now.timeZoneAbbreviation()))

if now.isDaylightTime():
    print("The current date falls into DST time.")
else:
    print("The current date does not fall into DST time.")
