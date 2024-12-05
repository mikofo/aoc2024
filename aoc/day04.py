"""04: Ceres Search"""
import aoc.util

class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        super(Solver, self).__init__(input)
        self.matrix = input.splitlines()
        self.rows, self.cols = len(self.matrix), len(self.matrix[0])

    def is_in_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

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
        def is_cross(x, y):
            if x < 1 or y < 1 or y == self.cols - 1 or x == self.rows - 1:
                return False
            
            d1 = self.matrix[x-1][y-1] + self.matrix[x+1][y+1]
            d2 =  self.matrix[x-1][y+1] + self.matrix[x+1][y-1]

            if not (d1 == 'MS' or d1 == 'SM'):
                return False
            
            if not (d2 == 'MS' or d2 == 'SM'):
                return False
            
            return True
            
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 'A' and is_cross(i,j):
                    count += 1
                       
        return count