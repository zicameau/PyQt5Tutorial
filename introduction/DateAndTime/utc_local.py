#! /usr/bin/python3

""" This is an example that determines the current universal and local
 date and time. """


from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Local datetime: ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))
