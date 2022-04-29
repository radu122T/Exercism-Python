# nstructions
# A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,

# a**2 + b**2 = c**2
# and such that,

# a < b < c
# For example,

# 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# Given an input integer N, find all Pythagorean triplets for which a + b + c = N.

# For example, with N = 1000, there is exactly one Pythagorean triplet for which a + b + c = 1000: {200, 375, 425}.

# NOTE: The description above mentions mathematical sets, but also that a Pythagorean Triplet {a, b, c} must be ordered such that a < b < c (ascending order). This makes Python's set type unsuited to this exercise, since it is an inherently unordered container. Therefore please return a list of lists instead (i.e. [[a, b, c]]). You can generate the triplets themselves in whatever order you would like, as the enclosing list's order will be ignored in the tests.

import math
def triplets_with_sum(number):
	N=float(number)
	triplets = []
	for c in range(int(N/2)-1,int((math.sqrt(2)-1)*N),-1):
		D = math.sqrt(c**2 - N**2 + 2*N*c)
		if D==int(D):
			triplets.append([int((N-c-D)/2),int((N-c+D)/2),c])
	return triplets

#import math
# def triplets_with_sum(number):
#     x = []
#     z = []
#     for b in range(number):
#         for a in range(1, b):
#             c = math.sqrt( a * a + b * b)
#             if c % 1 == 0:
#                 x.append([a, b, int(c)])
#     for i in x:
#         if sum(i) == number and i[0]<i[1]<i[2]:
#             z.append(i) 
#     return z