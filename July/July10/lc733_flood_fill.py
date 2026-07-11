class Solution:
    def floodFill(self, image, sr, sc, color):

        rows, cols= len(image), len(image[0])
        home_pixel = image[sr][sc]

        if home_pixel == color:
            return image

        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        stack = [(sr,sc)]
        visited = set()

        while stack:
            curr_node = stack.pop()
            if curr_node in visited:
                continue
            visited.add(curr_node)

            r, c = curr_node
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and image[nr][nc] == home_pixel):
                    stack.append((nr, nc))
            
        return image
