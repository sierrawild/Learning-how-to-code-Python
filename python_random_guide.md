# Python's `random` Library Guide

## What is the `random` module?

The `random` module generates pseudo-random numbers — they *look* random but are actually deterministic (if you set a seed, you get the same sequence every time). It uses the Mersenne Twister algorithm under the hood.

**Important:** Don't use this for security or cryptography — use the `secrets` module for that.

## Core Concept: `random.random()`

Everything else builds on `random.random()`, which returns a float between `0.0` and `1.0` (never quite reaching 1.0):

```python
import random
random.random()  # e.g., 0.37444887175646646
```

## Functions You'll Use Most in Creative Coding

### For integers:

- `randint(a, b)` — random integer from a to b *inclusive* (both endpoints included)
- `randrange(start, stop, step)` — like `range()` but picks one value randomly

```python
random.randint(1, 6)        # dice roll: 1, 2, 3, 4, 5, or 6
random.randrange(0, 100, 5) # 0, 5, 10, 15, ..., 90, or 95
```

### For floats:

- `uniform(a, b)` — random float between a and b

```python
random.uniform(2.5, 10.0)  # e.g., 3.1800146073117523
```

### For sequences (lists, tuples, etc.):

- `choice(seq)` — pick one random element
- `shuffle(seq)` — rearrange a list in place
- `sample(seq, k)` — pick k unique elements without replacement

```python
colors = ['red', 'blue', 'green', 'yellow']
random.choice(colors)           # e.g., 'blue'
random.shuffle(colors)          # modifies colors in place
random.sample(colors, 2)        # e.g., ['green', 'red']
```

### Weighted choices:

- `choices(population, weights, k)` — pick k elements *with replacement*, optionally weighted

```python
# Pick 10 colors, but red is twice as likely as the others
random.choices(['red', 'blue', 'green'], weights=[2, 1, 1], k=10)
```

## Controlling Randomness: Seeds

Use `random.seed()` to get reproducible results — same seed = same sequence:

```python
random.seed(42)
print(random.random())  # always 0.6394267984578837
print(random.random())  # always 0.025010755222666936

random.seed(42)         # reset the seed
print(random.random())  # back to 0.6394267984578837
```

This is super useful when you're iterating on an animation — you can get the same "random" variation every time you run it.

## Distribution Functions (For Advanced Effects)

These generate numbers following statistical distributions — great for natural-looking variation:

- `gauss(mu, sigma)` — normal (bell curve) distribution, centered at `mu` with spread `sigma`
- `expovariate(lambd)` — exponential distribution (good for timing events)
- `triangular(low, high, mode)` — triangular distribution (peaks at `mode`)

```python
# Most values cluster around 50, with standard deviation of 10
random.gauss(50, 10)  # e.g., 47.3, 52.1, 49.8

# Useful for creating "clumpy" spacing rather than uniform
random.expovariate(1.0 / 5.0)  # average interval of 5
```

## Practical Example for py5

Here's how you might use `random` in a sketch:

```python
import py5
import random

def setup():
    py5.size(800, 600)
    py5.background(255)
    
    # Set seed for reproducible randomness
    random.seed(12345)
    
    # Draw 50 circles with random positions and sizes
    for _ in range(50):
        x = random.uniform(0, py5.width)
        y = random.uniform(0, py5.height)
        diameter = random.gauss(30, 10)  # average 30, some variation
        
        # Pick a random color from your palette
        color = random.choice(['#FF6B6B', '#4ECDC4', '#45B7D1'])
        py5.fill(color)
        py5.circle(x, y, diameter)
```

## Key Gotcha

`randint(1, 10)` includes both 1 *and* 10 (unlike `range(1, 10)` which stops at 9). This trips people up!

## Additional Resources

- [Official Python documentation](https://docs.python.org/3/library/random.html)
- Use `random.seed()` for reproducible "randomness" during development
- For truly unpredictable numbers (security/crypto), use the `secrets` module instead
