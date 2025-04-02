
def twosum(nums, target):
    seen = {}
    
    for i in range (len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
    return []

# Test cases
print(twosum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twosum([3, 2, 4], 6))       # Output: [1, 2] 
print(twosum([3, 3], 6))          # Output: [0, 1]
print(twosum([1, 2, 3, 4, 5], 10)) # Output: []
print(twosum([0, 4, 3, 0], 0))    # Output: [0, 3]
print(twosum([1, 2, 3, 4, 5], 6)) # Output: [1, 3]
    