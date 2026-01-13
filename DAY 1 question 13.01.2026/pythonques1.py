from functools import reduce

numbers = range(1, 21)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_evens = list(map(lambda x: x ** 2, even_numbers))

sum_of_squares = reduce(lambda x, y: x + y, squared_evens)

for index, value in enumerate(squared_evens):
    print(index, value)

print("Sum of squared even numbers:", sum_of_squares)
