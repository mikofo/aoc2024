"""01: PROBLEM NAME"""
import aoc.util
from collections import Counter


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)

        # optionally do something with self.input, like parsing it to a more
        # useful representation and storing it in the instance
        self.c1, self.c2 = map(list, zip(*[map(int, line.split()) for line in input.splitlines()]))
        self.c1.sort()
        self.c2.sort()

    def part_one(self) -> int:
        sum = 0
        for i in range(len(self.c1)):
            sum += abs(self.c1[i] - self.c2[i])
        return sum

    def part_two(self) -> int:
        sum = 0
        frequency = Counter(self.c2)
        for i in range(len(self.c1)):
            n = self.c1[i]
            sum += n * frequency.get(n, 0)
        return sum
