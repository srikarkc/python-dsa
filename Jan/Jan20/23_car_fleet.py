class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        stack = []

        for p, s in reversed(cars):
            time = (target - p) / 2
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)