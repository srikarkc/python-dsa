# Problem #79 - Word Search

Given an (m x n) grid of characters `board` and a string `word`. 

Return `true` if the word exists in the grid.

Adjacent cells are horizontally or vertically neighboring

## Thinking

Loop for getting every character:

```python
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j])
```

## Learning from chatGPT solution

DFS + back-tracking

### Backtracking

Backtracking is a problem-solving technique that builds a solution incrementally, and whenever it realizes the current path cannot lead to a valid solution, it undoes (backtracks) the last step and tries another possibility.