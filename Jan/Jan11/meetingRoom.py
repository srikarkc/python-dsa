class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]
            curr_start = intervals[1][0]

            if curr_start < prev_end:
                return False
            
        return True