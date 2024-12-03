"""03: Mull it Over"""
import aoc.util
import re
from typing import Tuple

reg = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        super(Solver, self).__init__(input)
        self.totals = self.parse()


    def parse(self) -> Tuple[int, int]:
        p1, p2 = 0, 0
        do = True
        for match in reg.finditer(self.input):
            if match.group(0) == 'do()':
                do = True
            elif match.group(0) == "don't()":
                do = False
            else:
                a, b = map(int, match.groups())
                p1 += a * b
                if (do):
                    p2 += a * b
        return [p1, p2]

    def part_one(self) -> int:
        return self.totals[0]

    def part_two(self) -> int:
        return self.totals[1]
