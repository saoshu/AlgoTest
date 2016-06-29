"""
find two integer numbers in a given list of integer which can add up to a given value

print these two numbers if found; 
print false if no matching
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


def find_two_numbers_add_up_to_target__sort_and_find(numbers, target):
	"""
	no hash map solution
	"""
	sorted_numbers = sorted(numbers)
	print sorted_numbers
	begin=0
	end=len(numbers)-1
	found = False
	pairs = []
	while(begin<end):
		if sorted_numbers[begin] + sorted_numbers[end] > target:
			end-=1
		elif sorted_numbers[begin] + sorted_numbers[end] < target:
			begin+=1
		else:
			found = True
			pairs.append((begin+1, end+1))
			begin +=1
			end-=1
	return [pairs[0][0], pairs[0][1]]
	# print found, pairs

def find_two_numbers_add_up_to_target__hash(numbers, target):
	"""
	hash map solution
	"""
	map = {}
	for n in numbers:
		map[n] = target - n

	found = False
	for k in map.keys():
		if map[k] in map.keys():
			found = True
			print k, map[k]

	if not found:
		print "no matching"

if __name__ == "__main__":
	# numbers = [1.0, -40, 31, 52, 18, -30, 99, -50, 98, 97, -51, 99, 98]
	numbers = [100, 99, 98, 97, 8, 96, 95, 7, 94, 93, 92, 0]
	# numbers = [1.0, 40]
	# find_two_numbers_add_up_to_target__hash(numbers, 100)
	print find_two_numbers_add_up_to_target__sort_and_find(numbers, 100)

