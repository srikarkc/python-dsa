class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:
            if start > cur_end:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = start, end
            else:
                cur_end = max(cur_end, end)

        merged.append([cur_start, cur_end])

        