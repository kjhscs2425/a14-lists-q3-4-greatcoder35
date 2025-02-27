def average(numbers):
    "Return the average of a list of numbers"
    # YOUR CODE HERE
    divisor = len(numbers)
    for amount in numbers:
        total = sum(numbers)
        avg = total / divisor
        return avg

print(average([32, 78, 48, 71, 93, 71, 79, 44, 5, 42])) #56.3
print(average([5, 4, 3, 2, 1])) # 3.0
print(average([8.0, 3.14159, 17])) # 9.38053