# Python3 code to implement the approach

# Function to find the most frequent element
def findMostFrequent(arr, n):

	# Map to store the frequency
	# of each character
	unmap = {}
	for i in range(n):
		for j in range(n):
			if unmap.get(arr[i][j]) != None:
				unmap[arr[i][j]] = unmap[arr[i][j]]+1
			else:
				unmap[arr[i][j]] = 1

	# To store the frequency of character
	arr2 = []
	for ele1, ele2 in unmap.items():
		temp = [ele2, ele1]
		arr2.append(temp)

	# Sort the array
	arr2.sort(reverse=True)
	return arr2

# Driver code
if __name__ == '__main__':

	# Size of the matrix
	N = 3

	# Initialize the 2D array
	arr = [['a', 'a', 'a'], ['b', 'a', 'c'], ['d', 'c', 'a']]

	# Function call
	ans = findMostFrequent(arr, N)
	
	# Print the answer
	for i in range(0, len(ans)):
		print(ans[i][1], ":", ans[i][0])

# This code is contributed by Rohit Pradhan
