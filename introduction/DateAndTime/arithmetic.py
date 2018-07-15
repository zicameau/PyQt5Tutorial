#!/usr/bin/python3

""" This example dtermines the current datetime and add or
subtracts days, seconds, months, and years."""

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Today:", now.toString(Qt.ISODate))
print("Adding 12 days: {0}".format(now.addDays(12).toString(Qt.ISODate)))
print("Subtracting 22 days: {0}".format(
    now.addDays(-22).toString(Qt.ISODate)))

print("Adding 50 seconds: {0}".format(
    now.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 months: {0}".format(
    now.addMonths(3).toString(Qt.ISODate)))
print("Adding 12 years: {0}".format(
    now.addYears(12).toString(Qt.ISODate)))

