import sys
import time

# Without yield
print("Without yield")
def square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

numbers = range(10_000)

start = time.time()
squares = square(numbers)
print(squares[:5])
print(f'It took {time.time() - start} seconds')
print(f"size: {sys.getsizeof(squares, 'bytes')} bytes")

# With yield
print("with yield")
def square_yield(numbers):
    for number in numbers:
        yield number * number

start = time.time()
squares_yield = square_yield(numbers)
print(f'It took {time.time() - start} seconds')
print(f"size: {sys.getsizeof(squares_yield, 'bytes')} bytes")


print(next(squares_yield))
print(next(squares_yield))
print(next(squares_yield))
print(next(squares_yield))


# Using list comprehention - generators
print("Using list comprehention with generators")

start = time.time()
squares_yield = (i*i for i in numbers)
print(f'It took {time.time() - start} seconds')
print(f"size: {sys.getsizeof(squares_yield, 'bytes')} bytes")

print(next(squares_yield))
print(next(squares_yield))
print(next(squares_yield))
print(next(squares_yield))

# Using list comprehention - array
print("Using list comprehention with generators")

start = time.time()
squares = [i*i for i in numbers]
print(f'It took {time.time() - start} seconds')
print(f"size: {sys.getsizeof(squares, 'bytes')} bytes")
