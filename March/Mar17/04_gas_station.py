class Solution:
    def canCompleteCircuit(self, gas, cost):
        # If total gas is less than total cost, it's impossible
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # If we run out of fuel at this step
            if total_tank < 0:
                # Pick the next station as the new starting point
                start_index = i + 1
                # Reset our current tank for the new start
                total_tank = 0

        return start_index