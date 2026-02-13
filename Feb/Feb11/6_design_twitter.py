import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId), ...]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            tlist = self.tweets[followee]
            if tlist:
                idx = len(tlist) - 1
                time, tid = tlist[idx]
                heapq.heappush(heap, (time, tid, followee, idx - 1))

        while heap and len(res) < 10:
            time, tid, u, next_idx = heapq.heappop(heap)
            res.append(tid)

            if next_idx >= 0:
                ntime, ntid = self.tweets[u][next_idx]
                heapq.heappush(heap, (ntime, ntid, u, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
