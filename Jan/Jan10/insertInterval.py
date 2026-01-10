class Solution:
    def insertInterval(self, intervals, newInterval):
        res = []
        s, e = newInterval
        n = len(intervals)
        i = 0

        # 1 - Add intervals completely before newIntervals
        while i < 0 and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # 2 - Merge overlapping intevals into newInterval
        while i < 0 and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1

        res.append([s, e])

        # 3 - Merge the remaining
        while i < n:
            res.append(intervals[i])
            i += 1

        return res