class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	def __str__(self):
		return self.value

def build_bs_tree_from_list(values):
	root = Node(values[0])
	
	node = Node(value)
	if (value <= root.value):
		root.left = node
		build_bs_tree_from_list(values)
		
def main():
	print build_bs_tree_from_list([3,4,5,7,8])

if __name__ == "__main__":
	main()