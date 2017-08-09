#                                                   #
#  See my progress and notes on Github at           #
#  https://github.com/AllenTuring/GoogleChallenge   #
#___________________________________________________#

import math

# Find the maximum number of henchmen you can pay
# Being stingy as possible (using Fibonacci pattern)
def find_maximum_henchmen(total_lambs):
	# TODO stub
	return 0

# Find the minimum number of henchmen you can pay
# Being generous as possible (using 2^n pattern)
def find_minumum_henchmen(total_lambs):
	# henchmen paid so far is n
	n = 0
	# max pay all of the minions you can
	# yes, we can optimize this with log later
	while total_lambs >= 2**n:
		total_lambs -= 2**n
		n += 1

	# Are there enough left to pay another without breaking the fib rule?
	# Can be optimized as (2**(n-1)) * 3
	last2 = 2**n + 2**(n - 1)
	if total_lambs >= last2:
		n += 1

	# Total minions paid.
	return n

# Return the diff between the minimum and maximum
def answer(total_lambs):
	return find_maximum_henchmen(total_lambs) - find_minumum_henchmen(total_lambs)

###### UNIT TESTS ######
def test():
	test_answer()
	test_max()
	test_min()

def test_answer():
	assert answer(1) == 0
	assert answer(10) == 1

def test_max():
	assert find_maximum_henchmen(1) == 1
	assert find_maximum_henchmen(10) == 4

def test_min():
	assert find_minumum_henchmen(1) == 1
	assert find_minumum_henchmen(10) == 3
