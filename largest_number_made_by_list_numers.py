def comp(x, y):
	n1 = 0
	tmp = x
	while(tmp/10>0):
		n1 += 1
		tmp = tmp/10

	n2 = 0
	tmp = y
	while (tmp/10>0):
		n2 += 1
		tmp = tmp/10

	if (n1 < n2):
		x = x * 10**(n2-n1) + y/(10**(n1+1))


	if (n1 > n2):
		y = y * 10**(n1-n2) + x/(10**(n2+1))

	return x>=y

if __name__ == "__main__":
	nums = [9,32,35,343,2,1]	
	print(nums.sort(comp))