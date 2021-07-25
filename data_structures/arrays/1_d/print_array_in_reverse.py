'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

# Print Array In Reverse

Given the size and the elements of array A, print all the elements in reverse order.

Input:
- First line of input contains, N - size of the array.
- Following N lines, each contains one integer, i{th} element of the array i.e. A[i].

Output:
Print all the elements of the array in reverse order, each element in a new line.

Constraints:
  1 <= N <= 100
  0 <= A[i] <= 1000

Sample input:
5
4
12
7
15
9

Sample output:
9
15
7
12
4
'''

# Write your code here
N = int(input())
array = [0] * N

for i in range(N-1, -1, -1):
    array[i] = int(input())

for i in range(0, N):
    print(array[i])