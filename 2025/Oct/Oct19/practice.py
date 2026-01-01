intervals = [(0, 5), (15, 20)]

def canMeetingHappen(intervals):
    interval_length = len(intervals)

    for i in range(interval_length):
        A = intervals[i]
        for j in range(i + 1, interval_length):
            B = intervals[j]

            if min(A.end, B.end) > max(A.start, B.start):
                return False
            
    return True

def canAttendMeetings(intervals):
    intervals.sort(key=lambda i: i.start)

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False
        
        return True