#!/usr/bin/python3
import os
import signal

# graceful exit on [ctrl] + c
def signal_handler(sig, frame):
	print()
	quit()
signal.signal(signal.SIGINT, signal_handler)

failures = False

# sample size
def getN():
	while True:
		try:
			test = int(input("Enter total sample size: "))
			if test > 3:
				break
			print("Requires integer greater than 3")
		except Exception as e:
			print(e)
	return [i for i in range(1, test + 1)]

# possible success
def getM():
	while True:
		try:
			test = int(input("Enter possible successes: "))
			if test < N[-1] and test > 0:
				break
			print("Possible successes must be between 0 and " + str(N[-1]))
		except Exception as e:
			print(e)
	return [i for i in range(1, test + 1)]

# required successes
def getK():
	while True:
		try:
			test = int(input("Enter required number of successes: "))
			if test == 0:
				global failures
				failures = True
				return [i for i in range(1, N[-1] - M[-1] + 1)]
			if test <= M[-1]:
				break
			print("Required successes must be less than or equal to " + str(M[-1]))
		except Exception as e:
			print(e)
	return [i for i in range(1, test + 1)]

# trials
def getT():
	while True:
		try:
			test = int(input("Enter number of trials: "))
			if failures and (test >= 1) and (test <= N[-1]):
				break
			if (test >= K[-1]) and (test <= N[-1]):
				break
			if failures:
				print("Trials must be between 1 and " + str(N[-1]))
			else:
				print("Trials must be between " + str(K[-1]) + " and " + str(N[-1]))
		except Exception as e:
			print(e)
	return [i for i in range(1, test + 1)]

# possible failures
def getG():
	return [i for i in range(1, N[-1] - M[-1] +1)]

# required failures
def getH():
	if K == T:
		return [0]
	else:
		return [i for i in range(1, T[-1] - K[-1] + 1)]

# factorial
def factory(list):
	i = 0
	e = 1
	for i in list:
		e = e*i
	return(e)

# denominator
def getdenom(a, b):
	return  [i for i in range(1, b + 1)]

# numerator
def getnum(a, b):
	if a == b:
		return [1]
	else:
		return a[a[-1] - b[-1]:]

if __name__ == "__main__":
	escape = "[Enter] to exit"
	N = getN()
	M = getM()
	K = getK()

	# if you're testing for 0 failures, you're actually testing for 1 - chance of successes
	if failures:
		V = M
		M = K
		K = V

	T = getT()

	# sanity check 2
	if K[-1] == M[-1] and T[-1] == N[-1]:
		print("100.000%")
		input(escape)
		exit()

	# sanity check 3
	if T == [1]:
		if failures:
			print("{0:.3%}".format(M[-1] / N[-1]), 'chance of 0 successes.')
			print("a")
			input(escape)
			exit()
		else:
			print("{0:.3%}".format(M[-1] / N[-1]))
			input(escape)
			exit()

	# sanity check 4
	if failures:
		K = T
		# if you draw the whole deck and require 0 failures, you fail.
		if T[-1] == N[-1] and M[-1] > 0:
			print('0.000%')
			print()
			input(escape)
			exit()

	G = getG()
	H = getH()

	topleftnum = getnum(M, K)
	topleftdenom = getdenom(M[-1], K[-1])

	if (G == H):
		toprightnum = G
	else:
		toprightnum = getnum(G, H)

	toprightdenom = getdenom(G[-1], H[-1])
	bottomnum = getnum(N, T)
	bottomdenom = getdenom(N[-1], T[-1])

	topleftnum = factory(topleftnum)
	topleftdenom = factory(topleftdenom)

	toprightnum = factory(toprightnum)
	toprightdenom = factory(toprightdenom)

	bottomnum = factory(bottomnum)
	bottomdenom = factory(bottomdenom)

	if (T == [1]):
		top = K[-1]
		bottom = N[-1]
	else:
		topleft = topleftnum / topleftdenom
		topright = toprightnum / toprightdenom
		top = topleft * topright
		bottom = bottomnum / bottomdenom

	print()
	if failures:
		print("{0:.3%}".format(top / bottom) + " chance of 0 successes")
		print()
		input(escape)
	else:
		print("{0:.3%}".format(top / bottom))
		print()
		input(escape)
	exit()
