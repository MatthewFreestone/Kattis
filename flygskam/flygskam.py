# Rating: ~ 4.5 / 10
# Link: https://open.kattis.com/problems/flygskam

from collections import defaultdict
from math import pi, cos, sin, sqrt, atan2
from heapq import heappush, heappop
import sys


def distance(x,y):
  lat1, lon1 = x
  lat2, lon2 = y
  # m from center of earth
  radius = 6381000
  rad_lat_1 = lat1 * pi / 180
  rad_lat_2 = lat2 * pi / 180
  rad_d_lat = abs(rad_lat_2 - rad_lat_1)
  rad_d_lon = abs((lon2 - lon1) * pi/180)
  a = sin(rad_d_lat / 2) **2 + cos(rad_lat_1) * cos(rad_lat_2) * sin(rad_d_lon / 2) **2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  return (radius * c) / 1000
  

def main():
  n, m = map(int,input().split())
  s,t = input().split()
  # print(distance((59.6467921,17.9370443), (60.197646, 11.100008)))
  # airport -> {airport -> distance}
  distances = defaultdict(dict)
  locations = dict()
  for _ in range(n):
    name, lon, lat = input().split()
    locations[name] = (float(lon), float(lat))
  for _ in range(m):
    end1, end2 = input().split()
    # print(end1,end2, file=sys.stderr)
    length = distance(locations[end1], locations[end2])
    distances[end1][end2] = length
    distances[end2][end1] = length
  
  final_distances = {i: -1 for i in locations.keys()}
  to_compute = []
  heappush(to_compute, (0, s))
  while to_compute:
    dist, airport = heappop(to_compute)
    if final_distances[airport] != -1:
      continue
    final_distances[airport] = dist
    for dest in distances[airport].keys():
      if final_distances[dest] == -1:
        shame_cost = 100 + distances[airport][dest]
        heappush(to_compute, (dist + shame_cost, dest))
  print(final_distances[t])
      
  

if __name__ == "__main__":
  main()
