class EuclideanAlgorithm:
    def euclidean_algorithm(self, a, b):
        # This method implements the Euclidean algorithm to find the greatest common divisor (GCD) of two numbers.
        # The base case occurs when the second number (b) becomes 0. This assumes that the first number (a) is always greater.
        if b == 0:
            # When b equals 0, it means that a is the GCD.
            return a
        else:
            # Recursively call the method with b and the remainder of a divided by b.
            return self.euclidean_algorithm(b, a % b)

if __name__ == "__main__":
    try:
        # Ask the user for input numbers.
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        # Check for valid input (both numbers should be positive integers).
        if a <= 0 or b <= 0:
            raise ValueError("Input numbers must be positive integers.")

        # Instantiate the class and call the method to calculate the GCD.
        euclidean = EuclideanAlgorithm()
        gcd = euclidean.euclidean_algorithm(a, b)
        print("The GCD is", gcd)

    except ValueError as ve:
        # Handle invalid input error.
        print("Error:", ve)
