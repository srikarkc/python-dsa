# Brute force solution

def checkInclusion(s1, s2):
    s1 = sorted(s1)

    for i in range(len(s2)):
        for j in range(i, len(s2)):
            sub_str = s2[i:j+1]
            sub_str = sorted(sub_str)
            if sub_str == s1:
                return True
            
    return False


# Optimal sliding window solution

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s[i]) - ord('a')] += 1
        s2Count[ord(s[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1

    return matches == 26