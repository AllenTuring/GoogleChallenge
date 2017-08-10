#                                                   #
#  See my progress and notes on Github at           #
#  https://github.com/AllenTuring/GoogleChallenge   #
#___________________________________________________#

import math


# The maximum number of lambs we care about
upper_bound = 10**9

# Generates a table of maximum values for stingy payment
# Takes advantage of upper bound 10^9
def generate_max_fib_table():
	# List of running totals of fibonacci term payment plan minimums
	# for increasing numbers of minions to pay
	sums = []
	running_sum = 0

	# fibonacci term generator
	last_pay, current_pay = 0, 1
	while running_sum <= upper_bound:
		running_sum += current_pay
		# generate the fib terms and assign them
		last_pay, current_pay = current_pay, last_pay + current_pay
		# add it onto the table
		sums.append(running_sum)

	# output the lookup table
	return sums

# Saved sum bound table
# ideal data structure: linked list
max_fib_table = generate_max_fib_table()

# Find the maximum number of henchmen you can pay
# Being stingy as possible (using Fibonacci pattern)
def find_maximum_henchmen(total_lambs):
	# henchmen paid so far is n
	n = 0
	# min pay all of the minions you can
	while n < len(max_fib_table) and max_fib_table[n] <= total_lambs:
		n += 1

	# there cannot enough left to pay because we are at minimum
	# see notes.txt for informal proof outline
	# no adjustment needed, unlike in max pay mode

	# output
	return n

# Find the minimum number of henchmen you can pay
# Being generous as possible (using 2^n pattern)
def find_minumum_henchmen(total_lambs):
	# henchmen paid so far is n
	n = 0
	# max pay all of the minions you can
	n = total_lambs.bit_length() - 1 # ultra-fast equivalent of floor(log2())
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
	test_gen_fib()

def test_answer():
	assert answer(1) == 0
	assert answer(10) == 1

	# simple ranges
	# calculated by hand + inspection
	for i in range(2, 4):
		assert answer(i) == 0
	for i in range(4, 6):
		assert answer(i) == 1
	assert answer(6) == 0
	for i in range(7, 12):
		assert answer(i) == 1
	assert answer(12) == 2
	for i in range(13, 20):
		assert answer(i) == 1

	# problem scope upper bound
	# found by hand
	assert answer(10**9) == 12

def test_max():
	# given values
	assert find_maximum_henchmen(1) == 1
	assert find_maximum_henchmen(10) == 4

	# simple ranges
	# calculated by hand + inspection
	for i in range(2, 4):
		assert find_maximum_henchmen(i) == 2
	for i in range(4, 7):
		assert find_maximum_henchmen(i) == 3
	for i in range(7, 12):
		assert find_maximum_henchmen(i) == 4
	for i in range(12, 20):
		assert find_maximum_henchmen(i) == 5

	# derived range test
	# caution! scales as fib(n)
	a, b, cumulative = 1, 1, 1
	for n in range(1, 23):
		lower = cumulative
		a, b, cumulative = b, a + b, cumulative + b
		for i in range(lower, cumulative):
			assert find_maximum_henchmen(i) == n

	# problem scope upper bound
	# found by hand
	assert find_maximum_henchmen(10**9) == 42

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
	for i in range(13, 26):
		assert find_minumum_henchmen(i) == 4

	# derived range test
	# caution! scales as 2^n
	n_min, n_max = 0, 1 # base init values for range bounds
	for n in range(1, 18):
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

def test_gen_fib():
	# check that the first few terms are correct
	assert max_fib_table[0] == 1
	assert max_fib_table[1] == 1+1
	assert max_fib_table[2] == 1+1+2
	assert max_fib_table[3] == 1+1+2+3
	# check that the last term is big enough
	assert max_fib_table[len(max_fib_table)-1] > upper_bound
	# known generator for the fibonacci series
	a, b = 0, 1
	for i in range(1, len(max_fib_table)):
		a, b = b, a+b
		# check that each term of the fib is a valid differencing of max_fib_table
		assert max_fib_table[i] - max_fib_table[i-1] == b
