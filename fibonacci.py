def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage:
n_terms = 10
print(f"Fibonacci series up to {n_terms} terms:")
fibonacci(n_terms)
