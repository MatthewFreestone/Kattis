from sys import stdin
from heapq import heappush, heappop
from dataclasses import dataclass

@dataclass
class HeapItem:
    def __init__(self, level, name, valid):
        self.level = level
        self.name = name
        self.valid = valid
    
    def __lt__(self, other):
        return self.level < other.level
  

heap = []
name_to_object = {}
curr_time = 0


def add_name(name, curr_time, level):
    # intuition: we want to sort by level, then by creation time. 
    # as creation time increases, level increases 
    # (lower priority, treat older cats first)
    new_level = level+curr_time*(1/1_000_000)
    item = HeapItem(new_level, name, True)
    name_to_object[name] = item
    heappush(heap, item)

def remove_name(name):
    item = name_to_object.pop(name)
    item.valid = False

next(stdin)
for line in stdin:
    curr_time += 1
    q, *params = line.split()
    
    if q == '0':
        # add name severity
        name, level = params[0], -int(params[1])
        add_name(name, curr_time, level)
    elif q == '1':
        # update name severity_increase
        name, increase = params[0], -int(params[1])
        old_obj = name_to_object[name]
        remove_name(name)
        add_name(name, 0, old_obj.level+increase)
    elif q == '2':
        # treat name
        name = params[0]
        remove_name(name)
    else:
        # return cat we treat next
        # heap ensures that its the cat with highest severity and arrived first
        while heap:
            if not heap[0].valid:
                removed = heappop(heap)
                continue
            print(heap[0].name)
            break
        else: 
            print("The clinic is empty")
            