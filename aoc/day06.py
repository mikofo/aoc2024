"""06: Guard Gallivant"""
from typing import Tuple
import aoc.util
from multiprocessing import Pool

nextDir = {
    'u': 'r',
    'r': 'd',
    'd': 'l',
    'l': 'u'
}

class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        super(Solver, self).__init__(input)
        self.maze = input.replace('\n', '')
        self.maze_size = len(self.maze)
        self.rows = input.index("\n")
        self.cols = int(self.maze_size / self.rows)
        self.start = self.maze.index("^")
        self.seen = set()

    def getUp(self, n: int):
        return n - self.cols if n >= self.cols else None

    def getLeft(self, n: int):
        return n - 1 if n % self.cols != 0 else None

    def getRight(self, n: int):
        return n + 1 if (n + 1) % self.cols != 0 else None

    def getDown(self, n: int):
        return n + self.cols if n + self.cols < self.maze_size else None
    
    def getNext(self, n: int, dir: str):
        actions = {
            'u': self.getUp,
            'l': self.getLeft,
            'r': self.getRight,
            'd': self.getDown
        }
        return actions[dir](n)
    
    def getPrev(self, n: int, dir: str):
        actions = {
            'u': self.getDown,
            'l': self.getRight,
            'r': self.getLeft,
            'd': self.getUp
        }
        return actions[dir](n)
    
    def creates_loop(self, o: int):
        seen = set()
        direction = 'u'
        pos = self.start
        while pos is not None and not (pos,direction) in seen:
            seen.add((pos, direction))
            peek = self.getNext(pos, direction)
            if peek is not None and self.maze[peek] == '#' or peek == o:
                direction = nextDir[direction]
            else:
                pos = peek
                
        if pos == None:
            return False
        else:
            return True
            
    def part_one(self) -> int:
        direction = 'u'
        pos = self.start
        while pos is not None:
            self.seen.add(pos)
            peek = self.getNext(pos, direction)
            if peek is not None and self.maze[peek] == '#':
                direction = nextDir[direction]
            else:
                pos = peek

        return len(self.seen)
    
    def part_two(self) -> int:
        count = 0
    
        with Pool() as pool:
            indices_to_check = [i for i in range(self.maze_size) if i in self.seen and i != self.start]
            results = pool.map(self.creates_loop, indices_to_check)
            for result in results:
                if result == True:
                    count += 1

        return count
