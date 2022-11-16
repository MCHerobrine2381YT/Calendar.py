# import
import calendar
import time

# variable
year = 2022
month = 11

# loading
print("\rMaking calendar", end="")
time.sleep(1)
print("\rMaking calendar.", end="")
time.sleep(1)
print("\rMaking calendar..", end="")
time.sleep(1)
print("\rMaking calendar...", end="")

# calendar
time.sleep(1)
print("\r", calendar.month(year, month), end="")
