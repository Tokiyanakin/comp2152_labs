# Week 05 Lab: Recursion & Functions
# COMP2152 - Python Programming

print("Week 05 Lab: Recursion & Functions")

# ------------------------------------------------------------
# Question 1: Fibonacci Number (Recursion)
# ------------------------------------------------------------

def fib(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive case
    return fib(n - 1) + fib(n - 2)


print("\nQ1 - Fibonacci (0 to 10):")
for i in range(0, 11):
    print("F(" + str(i) + ") =", fib(i))

print("F(15) =", fib(15))
print("F(20) =", fib(20))


# ------------------------------------------------------------
# Question 2: FizzBuzz (Functions + conditionals)
# ------------------------------------------------------------

def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


print("\nQ2 - FizzBuzz (n=15):")
print(fizz_buzz(15))


# ------------------------------------------------------------
# Question 3: Binary Search (Iterative + Recursive)
# ------------------------------------------------------------

def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)


def search_recursive(nums, target):
    # wrapper for recursive search
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)


print("\nQ3 - Binary Search (basic tests):")
nums = [-1, 0, 3, 5, 9, 12]

print("Iterative target 9 ->", binary_search_iterative(nums, 9))
print("Recursive target 9 ->", search_recursive(nums, 9))
print("Iterative target 2 ->", binary_search_iterative(nums, 2))
print("Recursive target 2 ->", search_recursive(nums, 2))

print("\nDone.")