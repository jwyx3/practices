# https://leetcode.com/problems/design-snake-game/

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w = width
        self.h = height
        self.food = food
        self.score = 0
        self.snake = collections.deque([(0,0)])
        self.delta = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.visited = set((0,0))

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y = self.snake[-1]
        dx, dy = self.delta[direction]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= self.h or ny < 0 or ny >= self.w:
            return -1
        # remember current score
        score = self.score
        self.snake.append((nx, ny))
        if self.score < len(self.food):
            fx, fy = self.food[self.score]
            if nx == fx and ny == fy:
                self.score += 1
        # if score is not changed.
        if score == self.score:
            self.visited.discard(self.snake.popleft())
        # the tail may be removed. so check visited here.
        if (nx, ny) in self.visited:
            return -1
        self.visited.add((nx, ny))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
