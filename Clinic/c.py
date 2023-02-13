import sys
from heapq import heapify, heappop, heappush
from collections import namedtuple

Patient = namedtuple('Patient', 'priority name')
_, k = map(int,input().split())
patients = []
left_line = set()

output = []

for line in sys.stdin:
    vals = line.split()
    if vals[0] == '1':
        _, t, m, s = vals
        # treat each patient like they got there at time 0
        adjusted_time = int(t)*k
        heappush(patients, Patient(-int(s) + adjusted_time, m))
    elif vals[0] == '2':
        if len(patients) == 0:
            # print('doctor takes a break')
            output.append('doctor takes a break')
            continue
        # print(f"Patients: {patients}", file=sys.stderr)
        fastest = heappop(patients)
        while fastest[1] in left_line:
            fastest = heappop(patients)
        output.append(fastest[1])
        # print(fastest[1])
    elif vals[0] == '3':
        _, t, m = vals
        left_line.add(m)
print('\n'.join(output))