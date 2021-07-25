'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

# Maximize The Sum
You are given an array A of N integers. You want to choose some integers from the array subject to
the condition that the number of distinct integers chosen should not exceed K. Your task is to
maximize the sum of chosen numbers. 

You are given T test cases.

Input format
- The first line contains a single integer T denoting the number of test cases.
- The first line of each test case contains two space-separated integers N and K denoting
  the length of the array and the maximum number of distinct integers you can choose.
- The second line of each test case contains N space-separated integers denoting
  the integer array A.

Output format
For each test case(in a separate line), print the maximum sum you can obtain by choosing
some elements such that the number of distinct integers chosen is at most K. If you cannot
choose any element, output 0.

Constraints:
  1 <= T <= 1000
  1 <= K <= N <= 5 * 10^5
  -10^9 <= A[i] <= 10^9
  Sum of N over all test cases does not exceed 2 * 10^6

Sample input:
2
4 1
3 -1 2 5
4 2
2 1 2 5

Sample output:
5
9
'''

# Write your code here
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    psums = {}
    result = 0

    for a in array:
        if a in psums:
            psums[a] += a
        else:
            psums[a] = a

    for k in sorted(psums, key = psums.get, reverse=True)[0:K]:
        # Ignore negative partial sums (we want to max the sum)
        # We need to pick AT MOST K distinct integers so less
        # than K is fine as long as our sum is max
        if psums[k] < 0:
            break
        result += psums[k]

    print(result)