# Python Program for implementation of
# Recursive Bubble sort
class bubbleSort:
	"""
	bubbleSort:
		function:
			bubbleSortRecursive : recursive
				function to sort array
			__str__ : format print of array
			__init__ : constructor
				function in python
		variables:
			self.array = contains array
			self.length = length of array
	"""

	def __init__(self, array):
		self.array = array
		self.length = len(array)

	def __str__(self):
		return " ".join([str(x)
						for x in self.array])

	def bubbleSortRecursive(self, n=None):
		if n is None:
			n = self.length

		# Base case
		if n == 1:
			return

		# One pass of bubble sort. After
		# this pass, the largest element
		# is moved (or bubbled) to end.
		for i in range(n - 1):
			if self.array[i] > self.array[i + 1]:
				self.array[i], self.array[i +
				1] = self.array[i + 1], self.array[i]

		# Largest element is fixed,
		# recur for remaining array
		self.bubbleSortRecursive(n - 1)

# Driver Code
def main():
	array = [64, 34, 25, 12, 22, 11, 90]
	
	# Creating object for class
	sort = bubbleSort(array)
	
	# Sorting array
	sort.bubbleSortRecursive()
	print("Sorted array :\n", sort)


if __name__ == "__main__":
	main()

# Code contributed by Mohit Gupta_OMG,
# improved by itsvinayak
