1. Two Sum
	write a function called TwoSum(arr) that takes an array of integers stored in arr and determines if any two numbers (excluding the first element)  in the array can sum up to the first element in the array.

For example, if arr is [7,3,5,2, -4, 8, 11], then there are two pairs that sum to the number 7:[5,2] and [-4,11]. Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. Pairs should be sparated by a space, so for the example above, your proram would return: 5,2 -4,11.

2. Merge sort
	implement the merge sort alogarithm in python. Write a function that takes an unsortedlist of integers as input and returns the list sorted in ascending order.

Requirments:

	1. Your function shoul use the Merge Sort alogarithm
	2. Optimize your code for efficiency.
	3. Provide comments or explanations for any key steps or optimizations.

def merge_sort(arr)
	#Your implementation here
#test the function
unsorted_list = [64,34,25,12,22,11,90]
print (merge_sort(unsorted_list))



|Test Case|Input                |Expected Output     |
------------------------------------------------------
|1        |[38,27,43,3,9,82,10] |[3,9,10,27,38,43,82]|
|2        |[5,2,8,5,9,1,5,2]    |[1,2,2,5,5,5,8,9]   |
|3        |[42]                 |[42]                |
|4        |[1,2,3,4,5]          |[1,2,3,4,5]         |
|5        |[9,7,5,3,1]          |[1,3,5,7,9]         |
|6        |[-5,-2,-8,-1,-9]     |[-9,-8,-5,-2,-1]    |
|7        |[4,-2,7,1,-5,3]      |[-5,-2,1,3,4,7]     |

3. Merge sort desc
	Implement the Merge Sort alogarithm in python. Write a function that takes an unsorted list of integers as input and returns the list sorted in descending order.

Requirments:
	4. Your function should use the Merge Sort alogarithm.
	5. Optimize your code for efficiency.
	6. Provide comments or explanations for any key steps or optimizations.

def merge_sort_desc(arr):
	#Your Implementation here
#Test the function.
unsorted_list = [38,27,43,3,9,82,10]
print(merge_sort_desc(unsorted_list))

|Test Case|Input                |Expected Output     |
------------------------------------------------------
|1	      |[38,27,43,3,9,82,10] |[82,43,38,27,10,9,3]|
|2	      |[5,2,8,5,9,1,5,2]    |[9,8,5,5,2,2,1]     |
|3	      |[42]                 |[42]                |
|4	      |[1.2.3.4.5]          |[5,4,3,2,1]         |
|5	      |[9,7,5,3,1]          |[9,7,5,3,1]         |
|6	      |[-5,-2,-8,-1,-9]     |[-1,-2,-5,-8,-9]    |
|7	      |[4,-2,7,1,-5,3]      |[7,4,3,1,-2,-5]     |

4. Factorial Recursion

Write a recursive function in python to calculate te factorial of a none-negative integer n. The factorial of n is the product of all positive integers up to n.

Requirments:
	1. Your function should use recursion to calculate the factorial.
	2. Handle the base case appropriately.
	3. Optimize your code for efficiency.
	4. Provide comments or explenations for any key steps or optimizations

def factorial_recursive(n):
	#Your implementation here
#Test the function
n = 5
result = factorial_recursive(n)
print (result)

|Test Case|Input(n)|Expected Output|
------------------------------------
|1	      |0	   |1		       |
|2	      |1	   |1		       |
|3	      |5	   |120		       |
|4	      |7	   |5040	       |
|5	      |10	   |3628800	       |
|6	      |12	   |479001600      |
|7	      |3	   |6		       |
|8	      |8	   |40320	       |

5. Binary Search Implementation

Implement the Binary Search alogarithm in python. Write a function that takes a sorted list of integers and a target value as input. The function should return the index of the target value if it's present in the lis or -1 if the target values is not found.

Requirments:

	1. Your function should use the Binary Search alogarithm. handle the case where the list is empty.
	2. Handle the case where the list is empty.
	3. Provide comments or explanations for any key steps or optimizations.
	4. Return the index of element

def binary_search (arr, target):
	#Your implementation here
#Test the function
sorted_list = [1,2,3,4,5,6,7,8,9,10]
target_value = 7
result = binary_serach(sorted_list, target_value)
print(result)

|Test Case|Sorted list		     |Target Value|Expected Output|
---------------------------------------------------------------
|1	      |[1,2,3,4,5,6,7,8,9,10]|7	          |6	          |
|2	      |[2,4,6,,8,10,12,14,16]|10	      |4	          |
|3	      |[1,3,5,7,9,11,13,15]  |5	          |2	          |
|4	      |[10,20,30,40,50]	     |20	      |1	          |
|5	      |[5,10,15,20,25,30]	 |25	      |4	          |
|6	      |[1,3,5,7,9]		     |8	          |-1	          |
|7	      |[]			         |42	      |-1	          |