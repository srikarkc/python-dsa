# Meeting rooms problem revision

## Meetings rooms 1

### Problem description

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

You want to find the earlier of the 2 end times --> `min(A.end, B.end)`

Then, you want to find the later of the 2 start times --> `max(A.start, B.start)`

## Meetings rooms 2

### Problem description for mr2

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

