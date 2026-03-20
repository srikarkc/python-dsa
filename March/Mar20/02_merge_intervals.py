class Solution:
    def mergeIntervals(self, intervals):
        intervals.sort(key=lambda x:x[0])   # sort by start time

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged