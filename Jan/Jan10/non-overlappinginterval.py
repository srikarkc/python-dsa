# The key insight in this problem is that although it asks for 
# number of removed intervals. We focus on which intervals to keep.
# We keep the intervals that end the soonest - this leaves more
# room for future intervals.

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        # 1 - sort intervals by the end time
        intervals.sort(key=lambda x: x[1])
        removed = 0
        prev_end = intervals[0][1]

        # 2 - iterate through intervals
        for i in range(1,len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                removed += 1
            else:
                prev_end = end

        return removed