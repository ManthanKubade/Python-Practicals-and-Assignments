# Specified list
nums = [7, 8, 120, 25, 44, 20, 27]

# Create a new list with only odd numbers (removing evens)
nums = [x for x in nums if x % 2 != 0]

print(nums)
# Output: [7, 25, 27]
