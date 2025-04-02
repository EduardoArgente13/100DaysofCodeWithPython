def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else: seen.add(num)
    return False
# Test cases
print(containsDuplicate([1, 2, 3, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4]))  # Output: False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
print(containsDuplicate([]))  # Output: False