class Solution:
    def insertInterval(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        s, e = newInterval
        res = []

        # existing intervals
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # new interval
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][e])
            i += 1

        res.append([s, e])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res