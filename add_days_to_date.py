
import os, string

class Date(object):
	def __init__(self, year, month, day):
		self.Day = day
		self.Month = month
		self.Year = year
	def __str__(self):
		return "{0}-{1}-{2}".format(self.Year, self.Month, self.Day)

def days_in_year_month(year, month):
	month_days_map = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
	if month > 12 or month < 1:
		return 0
	days = month_days_map[str(month)]
	if year%400 == 0:
		days+=1

	return days

def add_days_to_date(date, days):
	"""
	Given a date, and a integer number of days, add them up, to return a new date
	"""
	day = date.Day + days
	month = date.Month
	year = date.Year
	while(day > days_in_year_month(year, month)):
		day -= days_in_year_month(year, month)
		month += 1
		if (month>12):
			year += 1
			month = 1
	return Date(year, month, day)

def main():

	cur_date = Date(2015,6,6)
	print add_days_to_date(cur_date, 365)

if __name__ == '__main__':
	main()
