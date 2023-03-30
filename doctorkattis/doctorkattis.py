from sys import stdin
from heapq import heappush, heappop
from pprint import pprint

input()
heap = []
name_to_object = {}
curr_time = 0

def add_name(name, curr_time, level):
    item = [level, curr_time, name, True]
    name_to_object[name] = item
    heappush(heap, item)

def remove_name(name):
    item = name_to_object.pop(name)
    item[-1] = False

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
        original_level, creation_time, _,  _ = name_to_object[name]
        remove_name(name)
        add_name(name, creation_time, original_level+increase)
    elif q == '2':
        # treat name
        name = params[0]
        remove_name(name)
    else:
        # return cat we treat next
        # heap ensures that its the cat with highest severity and arrived first
        while heap:
            level, curr_time, name, valid = heap[0]
            if not valid:
                removed = heappop(heap)
                # print("Removed", removed, "bc invalid")
                continue
            # print("Best:",best)
            print(name)
            break
        else: 
            print("The clinic is empty")
    # print(q, params)
    # pprint(heap)
            