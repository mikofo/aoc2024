# You can copy/paste this template to start a new day

"""02: PROBLEM NAME"""
import aoc.util

def is_safe(report):
    out = [False, False]
    def check_report(report):
        increasing = decreasing = True
        for i in range(1, len(report)):
            diff = abs(report[i] - report[i-1])
            if diff < 1 or diff > 3:
                return False
            if report[i] > report[i-1]:
                decreasing = False
            elif report[i] < report[i-1]:
                increasing = False
        return increasing or decreasing
    
    if check_report(report):
        return [True, True]
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if check_report(modified_report):
            out[1] = True
            break
    
    return out



# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)

        self.input = input.splitlines()
        self.counts = [0, 0]
        for l in range(len(self.input)):
            output = is_safe(list(map(int, self.input[l].split())))
            if (output[0]):
                self.counts[0] += 1
            if (output[1]):
                self.counts[1] += 1

    


    def part_one(self) -> int:
        return self.counts[0]
    

    def part_two(self) -> int:
        return self.counts[1]
    
