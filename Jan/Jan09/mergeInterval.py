class Solution:
    def mergedInterval(self, intervals):
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_start, last_end = merged[-1]

            if start > last_start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(last_end, end)
        
        return merged