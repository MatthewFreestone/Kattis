import sys
from heapq import heappush, heappop
n, k = map(int,input().split())
patients = []
for line in sys.stdin:
    c_line = line.split()
    if c_line[0] == '1':
        _, time_arrival, name, severity = c_line
        heappush(patients, [int(severity)-(k*int(time_arrival)), name, int(time_arrival), int(severity)])
    elif c_line[0] == '2':
        if not patients:
            print('doctor takes a break')
            continue
        _, curr_time = c_line
        # for x in patients:
        #     x[3] = x[2] + k*(int(curr_time) - x[1])
        #     # get the most urgent patient
        print(heappop(patients)[1])
        # patients.remove(most_urgent_patient)
        # print(most_urgent_patient[0])

    elif c_line[0] == '3':
        pass