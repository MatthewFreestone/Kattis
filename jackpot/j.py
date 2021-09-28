import math
def main():
	m = int(input())
	for _ in range(m):
		wheels = int(input())
		if wheels == 1:
			print(input())
			continue

		ins = map(int,input().split())
		lcm_c = 1 
		for i in ins:
			lcm_c = lcm(lcm_c, i)
			if lcm_c > 10**9:
				print("More than a billion.")
				break;
		if lcm_c <= 10**9:
			print(lcm_c)

def lcm(a,b):
	return abs(a*b) // math.gcd(a,b)
	
if __name__ == '__main__':
	main()