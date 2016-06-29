"""
given a prices list in a short time period
if you can just buy/sell once, can you find the max profit?
"""

def find_min(numbers):
	
	min_index = 0
	min = numbers[min_index]
	for n in range(len(numbers)):
		if min > numbers[n]:
			min = numbers[n]
			min_index = n

	return min, min_index

def find_max(numbers):
	max_index = 0
	max = numbers[max_index]
	for n in range(len(numbers)):
		if max < numbers[n]:
			max = numbers[n]
			max_index = n

	return max, max_index

def max_profit(prices):
	print "max_profit", prices
	max_price, max_price_index = find_max(prices)
	min_price, min_price_index = find_min(prices[:max_price_index+1])
	max_profit_1 = max_price - min_price
	if max_price_index+1 == len(prices):
		return max_profit_1
	else:
		return find_max([max_profit_1, max_profit(prices[max_price_index + 1:])])[0]

if __name__ == "__main__":
	# numbers = [1.0, -40, 31, 52, 18, -30, 99, -50, 98, 97, -51, 99, 98]
	# numbers = [100, 99, 98, 97, 96, 95, 94, 93, 92]
	# numbers = [1.0, 40]
	print max_profit(numbers)
