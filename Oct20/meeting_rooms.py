
from typing import List

# Define an Interval class
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def canAttendMeetings(intervals: List[Interval]) -> bool:
    n = len(intervals)
    for i in range(n):
        A = intervals[i]
        for j in range(i + 1, n):
            B = intervals[j]
            if min(A.end, B.end) > max(A.start, B.start):
                return False
    return True
    
intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
print(canAttendMeetings(intervals))


# Optimized solution

def canAttend(intervals):
    intervals.sort(key=lambda i: i.start)

    for i in range(1, len(intervals)):
        if intervals[i-1].end > intervals[i].start:
            return False
    
    return True