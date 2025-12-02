def perm_in_string(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s[i]) - ord('a')] += 1
        s2Count[ord(s[i]) - ord('a')] += 1

    if s1Count == s2Count:
        return True
    
    for right in range(len(s1), len(s2)):
        in_idx = ord(s2[right] - ord('a'))
        s2Count[in_idx] += 1

        left = right - len(s1)
        out_idx = ord(s2[left] - ord('a'))
        s2Count[out_idx] -= 1

        if s1Count == s2Count:
            return True
        
    return False




def perm_in_string(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s[i]) - ord('a')] += 1
        s2Count[ord(s[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1

    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        # char coming in
        idx_in = ord(s2[right] - ord('a'))
        s2Count[idx_in] += 1
        if s2Count[idx_in] == s1Count[idx_in]:
            matches += 1
        elif s2Count[idx_in] == s1Count[idx_in] + 1:
            matches -= 1

        # char going out
        idx_out = ord(s2[left] - ord('a'))
        s2Count[idx_out] -= 1
        if s2Count[idx_out] == s1Count[idx_out]:
            matches += 1
        elif s2Count[idx_out] == s1Count[idx_out] - 1:
            matches -= 1

        left += 1

    return matches == 26