'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

def solution(A):
    return sum(range(1, len(A) + 2)) - sum(A) # literally find the difference.

# why plus 2? Because of the 0th index, and then because the range function is exclusive of the last number. So, if the length of A is 4, the range would be 1, 2, 3, 4. So, the sum would be 10. But, the missing number is 5. So, you need to add 5 to the sum.