

def string_combination(char_list):
	"""
	a,b,c -> a, b, c, ab, ac, bc, abc

	recurrsive solution:
	a(b, c, bc) -> a, ab, ac, abc 
	"""
	print string_combination_helper(char_list, [])

def string_combination_helper(char_list, result):
	if (len(char_list) == 2):
		result.append(char_list[0])
		result.append(char_list[1]) 
		result.append("{0}{1}".format(char_list[0], char_list[1]))

	else:
		char_0 = char_list[0]
		temp_result = [char_0]
		string_combination_helper(char_list[1:], result)
		for char in result:
			temp_result.append("{0}{1}".format(char_0, char))
			
		result.append(temp_result)
	return result



if __name__ == "__main__":
	my_char_list = "abc"
	# string_combination(my_char_list)

	comp(0, 0)
	comp(351, 35)
	comp(33, 3333)

	print 10**2
	
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
