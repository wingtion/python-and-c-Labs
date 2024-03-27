# Q1:
# a function to calculate factorials
factorialValue = lambda n: 1 if n == 0 else n * factorialValue(n - 1)

# User input for n and x
n = float(input("Enter a value for n: "))
x = int(input("Enter a value for x: "))

# a list of the terms in the series
terms = [(n**i) / factorialValue(i) for i in range(x + 1)]

# sum the terms in the series
result = sum(terms)

# Printing the result
print(f"e^{n} = {result}")

# Q2:
# initializing the global variable
sum = 0


def recursive_sum(n):
    """
    This recursive function calculates the sum of the alternating harmonic series
    from 1 to n.
    """
    global sum

    # base case: when n is 0, return the current sum
    if n == 0:
        return sum

    # calculate the next term in the series
    term = ((-1) ** (n + 1)) / n

    # adding the term to the running sum
    sum += term

    # recursively calling the function with n-1
    recursive_sum(n - 1)

recursive_sum(8)
print(sum)