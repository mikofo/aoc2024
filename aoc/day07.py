"""07: Bridge Repair"""
import aoc.util
from typing import List
from multiprocessing import Pool

def cc(x: int, y: int) -> int:
    return int(f"{x}{y}")

def add(x: int, y:int) -> int:
    return x + y

def mul(x: int, y: int) -> int:
    return x * y

def reaches_target(target: int, sum: int, operands: List[int], operators):
    if sum > target:
        return False
    elif len(operands) == 0:
        return sum == target
    else:
        return any(reaches_target(target, operator(sum, operands[0]), operands[1:], operators) for operator in operators)
    
def process_line(target, operands):
    result = None
    if reaches_target(target, operands[0], operands[1:], [add, mul]):
        result = 'p1'
    elif reaches_target(target, operands[0], operands[1:], [add, mul, cc]):
        result = 'p2'

    return (target, result)
    

class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        super(Solver, self).__init__(input)
        lines = [line.split(": ") for line in input.splitlines()]
        lines = [(int(test), list(map(int, args.split()))) for test, args in lines]
        self.p1, self.p2 = 0, 0
        self.results = {'p1': 0, 'p2': 0}

        with Pool() as pool:
            results = pool.starmap(process_line, lines)

        for target, result in results:
            if result == 'p1':
                self.p1 += target
                self.p2 += target
            elif result == 'p2':
                self.p2 += target

            
    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2
