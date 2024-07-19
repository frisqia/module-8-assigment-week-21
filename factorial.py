def factorial_recursive(n):
    #Your implementation here
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
#Test the function
n = 5
result = factorial_recursive(n)
print(result)
