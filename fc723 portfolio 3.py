# This function implements the Euclidean algorithm to find the greatest common divisor (GCD) of two numbers.
def euclidean_algorithm(a, b):
    # The base case occurs when the second number (b) becomes 0. This assumes that the first number (a) is always greater.
    if b == 0:
        # When b equals 0, it means that a is the GCD.
        return a
    else:
        # Recursively call the function with b and the remainder of a divided by b.
        return euclidean_algorithm(b, a % b)

# Provide values for the two numbers and print the result.
gcd = euclidean_algorithm(23, 69)
print("The greatest common divisor of the two numbers is:", gcd)