"""
Documentation:
https://docs.python.org/3/library/random.html

Source code:
https://github.com/python/cpython/blob/3.14/Lib/random.py

"""

import random

a = 1
b = 2
start = 0
stop = 10
step = 2



random.seed(42) # initialize random number generator. Use this to get the same result by using same number as the seed
print(random.random())  # always 0.6394267984578837
print(random.random())  # always 0.025010755222666936

random.seed(42)         # reset the seed
print(random.random())  # back to 0.6394267984578837

####################################################################

random.random() # random float between 0.0 and 1.0
random.randint(a, b) # — random integer from a to b inclusive (both endpoints included)
random.uniform(a,b) # random float between a and b
random.randrange(start, stop, step) # — like range() but picks one value randomly

####################################################################

'''
For sequences (lists, tuples, etc.):

choice(seq) — pick one random element
shuffle(seq) — rearrange a list in place
sample(seq, k) — pick k unique elements without replacement
'''
colors = ['red', 'blue', 'green', 'yellow']
random.choice(colors)           # e.g., 'blue'
random.shuffle(colors)          # modifies colors in place
random.sample(colors, 2)        # e.g., ['green', 'red']

####################################################################

"""
Weighted choices:
choices(population, weights, k) — pick k elements with replacement, optionally weighted
"""
# Pick 10 colors, but red is twice as likely as the others
random.choices(['red', 'blue', 'green'], weights=[2, 1, 1], k=10)

####################################################################

"""
Distribution Functions (For Advanced Effects)
These generate numbers following statistical distributions — great for natural-looking variation:

gauss(mu, sigma) — normal (bell curve) distribution, centered at mu with spread sigma
expovariate(lambd) — exponential distribution (good for timing events)
triangular(low, high, mode) — triangular distribution (peaks at mode)
"""
# Most values cluster around 50, with standard deviation of 10
random.gauss(50, 10)  # e.g., 47.3, 52.1, 49.8

# Useful for creating "clumpy" spacing rather than uniform
random.expovariate(1.0 / 5.0)  # average interval of 5