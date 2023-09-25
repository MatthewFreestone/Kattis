from sys import stdin
from collections import namedtuple

HeapNode = namedtuple('HeapNode', 'key value')
class IndexedPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.index = {}

    def pop(self, key):
        curr_idx = self.index[key]
        to_yield = self.min_heap[curr_idx]

        last_item = self.min_heap.pop()
        if last_item.key == key or not self.min_heap:
            del self.index[last_item.key]
            return last_item
        
        self.min_heap[curr_idx] = last_item
        self.index[last_item.key] = curr_idx

        self.__heapify_down(last_item.key)

        del self.index[to_yield.key]
        return to_yield

    def push(self, key, value):
        to_add = HeapNode(key, value)
        new_idx = len(self.min_heap)
        self.index[key] = new_idx
        self.min_heap.append(to_add)
        self.__heapify_up(key)
        # your code here

    def popmin(self):
        last_item = self.min_heap.pop()
        if not self.min_heap:
            del self.index[last_item.key]
            return last_item
        
        to_yield = self.min_heap[0]
        self.min_heap[0] = last_item
        self.index[last_item.key] = 0

        self.__heapify_down(last_item.key)

        del self.index[to_yield.key]
        return to_yield

    def peek(self):
        return self.min_heap[0]

    def decrease_key(self, key, new_value):
        # because it's a decrease, we can only ever go up the min heap
        curr_idx = self.index[key]
        existing = self.min_heap[curr_idx]
        assert new_value <= existing.value
        self.min_heap[curr_idx] = HeapNode(key, new_value)
        self.__heapify_up(key)
    
    def __heapify_up(self, key):
        curr_idx = self.index[key]
        curr = self.min_heap[curr_idx]
        # if we're heapify-ing up, we should check if the parent is 
        # less than the value at the current node. If so, move parent down
        # continue until we can't move parent, then we place the curr at its destination
        
        # because of how we index, an odd number is a left child, and an even number is right child
        while curr_idx > 0:
            # this changes either 2i+1 or 2i+2 into 2i
            offset = (curr_idx % 2) - 2
            parent_idx = (curr_idx + offset) // 2
            parent = self.min_heap[parent_idx]

            if curr.value < parent.value:
                self.min_heap[curr_idx] = parent
                self.index[parent.key] = curr_idx
                curr_idx = parent_idx
            else:
                break
        self.min_heap[curr_idx] = curr
        self.index[curr.key] = curr_idx

    def __heapify_down(self, key):
        curr_idx = self.index[key]
        curr = self.min_heap[curr_idx]
        heap_len = len(self.min_heap)
        # if we're heapify-ing down, we should check if either child is 
        # less than the value at the current node. If so, move child to parent spot
        # then, continue going down trying to place the original
        l_child_idx = curr_idx*2 + 1
        r_child_idx = l_child_idx + 1

        while l_child_idx < heap_len:
            if self.min_heap[l_child_idx].value < curr.value: 
                # perfer taking right to maintain complete trees
                if r_child_idx < heap_len and self.min_heap[r_child_idx].value <= self.min_heap[l_child_idx].value:
                    right_key = self.min_heap[r_child_idx].key
                    self.index[right_key] = curr_idx
                    self.min_heap[curr_idx] = self.min_heap[r_child_idx]
                    curr_idx = r_child_idx
                else:
                    left_key = self.min_heap[l_child_idx].key
                    self.index[left_key] = curr_idx
                    self.min_heap[curr_idx] = self.min_heap[l_child_idx]
                    curr_idx = l_child_idx
            elif r_child_idx < heap_len and self.min_heap[r_child_idx].value < curr.value:
                right_key = self.min_heap[r_child_idx].key
                self.index[right_key] = curr_idx
                self.min_heap[curr_idx] = self.min_heap[r_child_idx]
                curr_idx = r_child_idx
            else:
                break
            l_child_idx = curr_idx*2 + 1
            r_child_idx = l_child_idx + 1
        self.index[key] = curr_idx
        self.min_heap[curr_idx] = curr

    def __len__(self):
        return len(self.min_heap)
    def __bool__(self):
        return bool(self.min_heap)
    def __getitem__(self, key):
        # will throw key error if bad
        idx = self.index[key]
        return self.min_heap[idx].value

input()
heap = IndexedPriorityQueue()
curr_time = 0

def add_name(name, curr_time, level):
    value = (level, curr_time)
    heap.push(name, value)

def remove_name(name):
    heap.pop(name)

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
        original_level, creation_time = heap[name]
        heap.decrease_key(name, (original_level+increase, creation_time))

    elif q == '2':
        # treat name
        name = params[0]
        heap.pop(name)
    else:
        # return cat we treat next
        # heap ensures that its the cat with highest severity and arrived first
        if heap:
            name = heap.peek()
            print(name.key)
        else: 
            print("The clinic is empty")
            