def lengthOfLongestSubstring(s):
    chars = set()
    left, max_len = 0, 0

    for right, ch in enumerate(s):
        while ch in chars:
            chars.remove(s[left])
            left += 1
        
        chars.add(ch)
        max_len = max(max_len, right - left + 1)

    return max_len