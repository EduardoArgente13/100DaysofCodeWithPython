def lengthOfLongestSubstring(s):
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

print(lengthOfLongestSubstring("abcabcbb"))  # ✅ 3
print(lengthOfLongestSubstring("bbbbb"))  # ✅ 1
print(lengthOfLongestSubstring("pwwkew"))  # ✅ 3
print(lengthOfLongestSubstring(""))  # ✅ 0
print(lengthOfLongestSubstring("dvdf"))  # ✅ 3
