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
	n = math.floor(math.log(total_lambs, 2))
	total_lambs -= 2**n - 1

	# Are there enough left to pay another without breaking the fib rule?
	last_1 = 2**(n-1) if n > 0 else 0 # how much the last goon was paid
	last_2 = 2**(n-2) if n > 1 else 0 # how much 2nd-to-last goon was paid
	if total_lambs >= last_1 + last_2:
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
	# given values
	assert find_minumum_henchmen(1) == 1
	assert find_minumum_henchmen(10) == 3

	# simple ranges
	# calculated by hand + inspection
	for i in range(2, 6):
		assert find_minumum_henchmen(i) == 2
	for i in range(6, 13):
		assert find_minumum_henchmen(i) == 3

	# derived range test
	# caution! scales as 2^n
	n_min, n_max = 0, 1 # base init values for range bounds
	for n in range(1, 15):
		# we cycle the new range, calculating a new upper bound as
		# the sum of all terms 1, 2 ... 2^(n-2) for henchmen paid generously
		# plus the maximum amount of discardable leftover (last two dudes, with math.floor
		# to prevent partial-lamb payments to imaginary minions below the first one)
		n_min, n_max = n_max, (2**n - 1) + math.floor(2**(n-1)) + math.floor(2**(n-2))
		for i in range(n_min, n_max):
			# check every value in that range, just for goodness.
			assert find_minumum_henchmen(i) == n

	# problem scope upper bound
	# found by hand
	assert find_minumum_henchmen(10**9) == 30
