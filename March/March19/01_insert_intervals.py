class Solution:
    def insertIntervals(self, intervals, newInterval):
        result = []
        i, n = 0, len(intervals)

        # 1 - Add all intervals completely before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2 - Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[0], intervals[i][1])
            i += 1

        result.append(newInterval)

        # 3 - Add the rest
        while i < n:
            result.append(intervals[i])
            i += 1

        return result