#! /usr/bin/python3

""" This example calculates the number of days passed from the
last Xmas and the number of days until the next xmas. """

from PyQt5.QtCore import QDate

xmas1 = QDate(2016, 12, 24)
xmas2 = QDate(2017, 12, 24)

now = QDate.currentDate()

daysPassed = xmas1.daysTo(now)

print("{0} days have passed since last Xmas".format(daysPassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next Xmas".format(nofdays))
