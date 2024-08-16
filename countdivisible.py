'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''

# very naive solution, not efficient at all.

def solution(A, B, K):
    count = 0 
    for num in range(A, B):
        if num % K == 0:
            count += 1
    return count

# a one liner solution that happens to be more efficient.

'''
You first find the amount of times K goes into B and then the amount of times K goes into A. Take the difference of the two and you have the amount of numbers divisible by K between A and B.
Beware though, that there is the case of A being divisible by K. In that case, you need to disregard it to avoid redundancy.
'''

def solution(A, B, K):
    return B // K - (A - 1) // K
