

m = int(input()) # 2n-1 lines
n = (m+1)//2
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))

# #Another Method:



# # Write your solution here

# n=int(input())

# gap=((n+1)//2)-1

# for i in range(1,n+1,2):
#     print(' '*gap  +'*'*i)
#     gap-=1
    
# gap=1
# for i in range(n-2,0,-2):
#     print(' '*gap + '*'*i)
#     gap+=1

# Pattern Printing - Diamond
# Given an odd number n as an input print a diamond pattern with '*'' in n lines.

# Examples

# Input

# 3
# Output

#  *
# ***
#  *
# Input

# 5
# Output

#   *
#  ***
# *****
#  ***
#   *
# Input

# 7
# Output

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

