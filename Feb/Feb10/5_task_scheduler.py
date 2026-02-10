from collections import Counter

class Solution:
    def taskScheduler(self, tasks, n):
        task_freq = Counter(tasks)
        max_freq = max(task_freq.values())
        max_num = (1 for v in task_freq.values() if v == max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_num
        )