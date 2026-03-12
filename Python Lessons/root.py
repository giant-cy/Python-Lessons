# Method 1

# input_number = int(input("Enter a number: "))
# result  = input_number ** 0.5
# print(result)

# ----------------------------------------------------------------- #
# this is a GO script that Mohsen sent me
# func Sqrt(x float64) float64 {
# 	// Handle edge cases immediately
# 	if x < 0 {
# 		return math.NaN()
# 	}
# 	if x == 0 {
# 		return 0
# 	}
#
# 	// Initial guess: simple and effective start
# 	z := x / 2.0
#
# 	// Run until convergence
# 	for {
# 		// Newton's Method:
# 		// z_next = z - f(z)/f'(z)
# 		// f(z) = z^2 - x
# 		// f'(z) = 2z
# 		guess := z - (z*z-x)/(2.0*z)
#
# 		// Check convergence
# 		if math.Abs(z-guess) < epsilon {
# 			return guess
# 		}
#
# 		// Update guess
# 		z = guess
# 	}
# }


import math

def sqrt(number):
    if number < 0:
        return "negative number"
    if number == 0:
        return 0

    z = number / 2
    epsilon = 1e-10

    while True:
        guess = z - (z*z - number) / (2*z)
        if abs(z - guess) < epsilon:
            return guess
        z = guess

print(sqrt(9))
print(sqrt(2))