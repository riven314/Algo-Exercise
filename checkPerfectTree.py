# Using recursive method to check for perfect tree

class Tree(object):
	def __init__(self, id):
		self.x = id
		self.l = None
		self.r = None

def findDepth(root):
	depth = 1
	while (root.l != None):
		depth += 1
		root = root.l
	return depth

def checkPerfect(node, depth, level=0):
	if (node.l == None) and (node.r == None):
		return (depth == level+1)
	if (node.l == None) or (node.r == None):
		return False
	return checkPerfect(node.l, depth, level+1) and checkPerfect(node.r, depth, level+1)	
