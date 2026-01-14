# 1 to n number
class Iterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

        #fibonacci generator question
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

N = 5

print(" By Using Custom Iterator:")
for num in Iterator(N):
    print(num, end=" ")

print("\n\n By Using Generator:")
for fib in fibonacci_generator(N):
    print(fib, end=" ")

