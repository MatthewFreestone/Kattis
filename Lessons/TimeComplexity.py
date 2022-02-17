def printValues(n):
	for i in range(n):
		print(i)
		print(i)


def printValues(n):
	for i in range(n):
		for j in range(n):
			print(j)

def printValues(n):
	for i in range(n):
		for j in range(i):
			print(j)

def printValues(n):
	i=1
	while(i < n):
		print(i)
		i = i * 2

def printHello(n):
	print("Hello World")

def printValues(n):
	for i in range(10):
		print(i)

def sumValues(A):
	n = len(A) 
	for value in A:
		total += value



def findValue(A,value):
	n = len(A)
	for i in range(n):
		if A[i] == value:
			return true
	return false 

def findValueInList(A: list,value):
	n = len(A) 
	return value in A

def findValueInSet(A: set,value):
	n = len(A)
	return value in A

def addValueToSet(A: set, value):
	n = len(A)
	A.add(value)

def sortArray(A: list):
	n = len(A) 
	return sorted(A)

def addValueEndOfList(A: list, value):
	n = len(A)
	A.append(value)

def deleteFromMiddleofList(A: list, value):
	n = len(A)
	A.delete(n//2)

def addValueToStartOfList(A: list, value):
	n = len(A)
	A.insert(value, 0)