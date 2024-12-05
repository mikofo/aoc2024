"""05: Print Queue"""
import aoc.util
from functools import cmp_to_key

class TrieNode:
    def __init__(self):
        self.children = {}
        self.values = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key, value):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.values.update({value})

    def compare(self, key, number):
        node = self.root
        for char in key:
            if char not in node.children:
                return 0
            node = node.children[char]
        return -1 if number in node.values else 1

    def is_before(self, key, numbers):
        node = self.root
        for char in key:
            if char not in node.children:
                return []
            node = node.children[char]
        return [num for num in numbers if num in node.values]



class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        super(Solver, self).__init__(input)
        specs, updates = input.strip().split("\n\n")
        self.updates = list(update.split(",") for update in updates.split("\n"))
        self.specs = Trie()
        self.p1 = 0
        self.p2 = 0
        
        for spec in specs.splitlines():
            x,y = spec.split("|")
            self.specs.insert(x, y)

        for update in self.updates:
            if self.is_valid_update(update):
                self.p1 += int(update[len(update) // 2])
            else:
                valid_update = self.make_valid(update)
                self.p2 += int(valid_update[len(valid_update) // 2])

    def is_valid_update(self, update):
        for i in range(len(update) - 1, -1, -1):
            if len(self.specs.is_before(update[i], update[:i])) > 0:
                return False
        return True
    
    def make_valid(self, update):
        return sorted(update, key=cmp_to_key(self.specs.compare))

    def part_one(self) -> int:
        return self.p1
        

    def part_two(self) -> int:
        return self.p2
