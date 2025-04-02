def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    letter_count = {}

    for char in s:
        letter_count[char] = letter_count.get(char, 0) + 1

    for char in t:
        if char not in letter_count:
            return False
    letter_count[char] -= 1
    if letter_count[char] < 0:
        return False
    
    return True

# Test cases
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
print(isAnagram("a", "ab"))              # Output: False