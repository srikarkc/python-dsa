import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId, tweetId):
        self.time -= 1
        self.tweets[userId].append((self.time, tweedId))

    def getNewsFeed(self, userId):
        res = []
        heap = []

        # Ensure user follows themselves so that they see their own tweets
        self.following[userId].add(userId)

        for followee in self.following[userId]:
            tlist = self.tweets[followee]
            if tlist:
                idx = len(tlist) - 1
                time, tid = self.tweets[idx]
                heapq.heappush(heap, (time, tid, followee, idx - 1))

        while heap and len(res) < 10:
            time, tid, u, next_idx = heapq.heappop(heap)
            res.append(tid)
            if next_idx >= 0:
                ntime, ntid = self.tweets[next_idx]
                heapq.heappush(heap, (ntime, ntid, u, next_idx - 1))

        return res

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)