#/bin/python

print()

# total sample
N = [i for i in range(1, int(input("Enter total sample size: ")) + 1)]

if (N == []):
	print()
	print('I have nothing to test.')
	exit()

# possible success
M = [i for i in range(1, int(input("Enter possible successes: ")) + 1)] 

if (M == []):
	print()
	print('0.000%')
	exit()

if (N == [1]) and ( M == [1]):
	print()
	print('100.000%')
	exit()

if (M > N):
	print()
	print('Possible successes must be less than sample size.')
	exit()

# required success
k = [i for i in range(1, int(input("Enter required successes: ")) + 1)]

if (k == []):
	print()
	print('Requires non-zero. Try testing for', N[-1] - M[-1] ,'failure/s instead.')
	exit()

if (k[-1] > M[-1]):
	print()
	print('0.000%')
	exit()

# trials
n = [i for i in range(1, int(input("Enter number of trials: ")) + 1)] 

if (n == [0]):
	print()
	print('0.000%')
	exit()

# possible failures
g = [i for i in range(1, N[-1] - M[-1] + 1)]

# required failures
if (k == n):
	h = [1]
else:
	h = [i for i in range(1, n[-1] - k[-1] + 1)]

# getdenom
def getdenom(a, b):
	denominator = [i for i in range(1, b + 1)]
	return(denominator)

# getnum
def getnum(a, b):
	if (a == b):
		numerator = [1]
	else:
		numerator = a[a[-1] - b[-1]:]
	return(numerator)

topleftnum = getnum(M, k)
topleftdenom = getdenom(M[-1], k[-1])

if (g == h):
	toprightnum = g
else:
	toprightnum = getnum(g, h)
toprightdenom = getdenom(g[-1], h[-1])

bottomnum = getnum(N, n)
bottomdenom = getdenom(N[-1], n[-1])

def factory(list):
	i = 0
	e = 1
	for i in list:
		e = e*i
	return(e)

topleftnum = factory(topleftnum)
topleftdenom = factory(topleftdenom)

toprightnum = factory(toprightnum)
toprightdenom = factory(toprightdenom)

bottomnum = factory(bottomnum)
bottomdenom = factory(bottomdenom)

if (n == [1]):
	top = k[-1]
	bottom = N[-1]
else:
	topleft = topleftnum / topleftdenom
	topright = toprightnum / toprightdenom
	top = topleft * topright
	bottom = bottomnum / bottomdenom

print()
print("{0:.3%}".format(top / bottom))
print()