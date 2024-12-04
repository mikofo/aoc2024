"""04: Ceres Search"""
import aoc.util

class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        super(Solver, self).__init__(input)
        self.matrix = [list(line) for line in input.splitlines() if line.strip()]
        self.rows, self.cols = len(self.matrix), len(self.matrix[0])

    def is_in_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols
    
    def is_diagonal(self, line1, line2):
        if line1[1] != line2[1]:
            return False
        if line1[0][1] == line1[1][1] or line1[2][1] == line1[1][1]:
            return False
        if line2[0][1] == line2[1][1] or line2[2][1] == line2[1][1]:
            return False
        return True

    def part_one(self) -> int:
        word = 'XMAS'
        word_length = 4
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def search(x, y, index, dx, dy):
            if index == word_length:
                return True

            nx, ny = x + dx, y + dy

            if not self.is_in_bounds(nx, ny) or self.matrix[nx][ny] != word[index]:
                return False

            return search(nx, ny, index + 1, dx, dy)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == word[0]:
                    for dx, dy in directions:
                        if search(i, j, 1, dx, dy):
                            count += 1
        return count

    def part_two(self) -> int:
        word = 'MAS'
        word_length = 3
        matches = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        def search(x, y, index, dx, dy, path):
            path.append((x, y))

            if index == word_length:
                matches.append(path[:])
                path.pop()
                return

            nx, ny = x + dx, y + dy

            if not self.is_in_bounds(nx, ny) or self.matrix[nx][ny] != word[index]:
                path.pop()
                return

            return search(nx, ny, index + 1, dx, dy, path)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == word[0]:
                    for dx, dy in directions:
                        search(i, j, 1, dx, dy, [])

        count = 0
        for i in range(len(matches)):
            for j in range(i+1, len(matches)):
                line1 = matches[i]
                line2 = matches[j]
                if self.is_diagonal(line1, line2):
                    count += 1
                
        return count