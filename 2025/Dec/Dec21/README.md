# Pacific Atlantic water flow

If you start from every cell and check whether you can reach the ocean - it would be very slow.

Start from the oceans and move inwards only to cells that could have flowed into them.

From the ocean border cell, you can move to a neighbor if the neighbor's height is >= current height.

Compute `reachable_pacific` and `reachable_atlantic`. Answer is the intersection of the 2 sets.

1. Pacific starts from all cells in the top row, all cells in the left column
2. Atlantic starts from all cells in the bottom row, all cells in the right column.
