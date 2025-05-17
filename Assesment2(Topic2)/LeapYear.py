#checking whether the given year is leap year or not
# Input from user
year = int(input("Enter a year: "))
# Check leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")