def fibonacci(n):
  """Calculates the fibonacci sequence up to n."""
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
