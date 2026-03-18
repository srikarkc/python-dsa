from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for num in hand:
            if count[num] > 0:
                start_count = count[num]

                for nextnum in range(num, num + groupSize):
                    if count[nextnum] < start_count:
                        return False
                    count[nextnum] -= start_count

        return True