#!/usr/bin/python3

"""
Notes:

Julian day refers to a continuous count of days since the
beginning of the Julian Period which is used mostly by astronomers.
(Do not confuse it with the Julian Calendar)

It started in 4713 BC. The Julian day number 0 is assigned to the
day starting at noon on January 1, 4713 BC.

The Julian Day Number (JDN) is the number of days elapsed since
the beginning of this period. The Julian Date (JD) is the Julian
day number for the preceding noon plus the fraction of the day
since that instant (Qt does not compute this fraction).

It is also used by the military and old mainframe computers.

In this example, we compute the Gregorian Date and the Julian
day for today.

"""

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print("Gregorian date for today: ", now.toString(Qt.ISODate))
print("Julian day for today: ", now.toJulianDay())

