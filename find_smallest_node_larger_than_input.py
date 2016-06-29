
from tree_util import *

def find_smallest_node_larger_than_input(root, value):
	"""
	@param root is a balanced binary search tree, left < root <= right
	
	Given a value, find the smallest node larger than input value

	example: a tree like this, Given value=6, it should return 5
				4
		3				7
	2				5		8

	"""
	cur_node = root




def main():
	print find_smallest_node_larger_than_input(build_tree_from_list((2,3,4,5,7,8)), 6)
