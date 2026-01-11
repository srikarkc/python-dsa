class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])

        removed = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # overlap detected
            if start < prev_end:
                removed += 1
            else:
                prev_end = end

        return removed