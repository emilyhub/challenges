# memoized version of fibonacci

def fibonacci(n):
    return fib(n, {})

def fib(n, memo):
    if n <= 2:
        return 1
    one = n - 1 in memo
    two = n - 2 in memo
    if one and two:
        memo[n] = memo[n - 1] + memo[n - 2]
     if one:
        memo[n] = memo[n - 1] + fib(n - 2, memo)
    if two:
        memo[n] = memo[n - 2] + fib(n - 1, memo)
    if not one and not two:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]