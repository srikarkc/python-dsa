class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)

        rooms = []

        for interval in intervals:
            if rooms and intervals.start >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, interval.start)

        return len(rooms)