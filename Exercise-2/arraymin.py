#  program to find minimum 
# in arr[] of size n 

# python function to find minimum 
# in arr[] of size n 
def smallest(arr,n): 

	# Initialize maximum element 
	mn = arr[0] 

	# Traverse array elements from second 
	# and compare every element with 
	# current min 
	for i in range(1, n): 
		if arr[i] < mn: 
			mn = arr[i] 
	return mn

# Driver Code 
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = smallest(arr,n) 
print ("smallest in given array is",Ans) 


