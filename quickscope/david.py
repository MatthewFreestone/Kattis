from sys import stdin

#record: (layer, age, vartype)
def clean(record):
	while len(record)>0:
		a = record[-1]
		if a[1] < cur_ages[a[0]]:
			record.pop()
		else:
			return

layer = 0
cur_ages = [0]
records = dict()

first_line = True
for line in stdin:
	if first_line:
		first_line = False
		continue
	if line[0]=="{":
		layer += 1
		if len(cur_ages)==layer:
			cur_ages.append(0)
	elif line[0]=="}":
		cur_ages[layer] += 1
		layer -= 1
	elif line[0]=="D":
		_, var, vartype = line.split()
		if var in records:
			clean(records[var])
			if len(records[var])>0 and records[var][-1][0]==layer:	#have already declared at this level
				print("MULTIPLE DECLARATION")
				exit()
			records[var].append((layer, cur_ages[layer], vartype))
		else:	#new variable so it's simple
			records[var] = [(layer, cur_ages[layer], vartype)]
	elif line[0]=="T":
		_, var = line.split()
		if var in records:
			clean(records[var])
			print(records[var][-1][2] if len(records[var])>0 else "UNDECLARED")
		else:
			print("UNDECLARED")