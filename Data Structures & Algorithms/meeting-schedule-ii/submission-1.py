"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Sort by end time - O(nlogn)
Track active rooms
Track max rooms
Using a (priority/already sorted dont need) queue, iterate through sorted list:
-Check top, if current start time < current end time:
    -Allocate new room, check max
-Else: Pop front queue
-Push current to queue

Loop is O(n)

'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)

        meetings = 0
        m_meetings = 0
        q = []

        for i in intervals:
            while len(q) > 0 and i.start >= q[0]:
                heapq.heappop(q)
                meetings -= 1
            heapq.heappush(q, i.end)
            meetings += 1
            m_meetings = max(m_meetings, meetings)
        
        return m_meetings






