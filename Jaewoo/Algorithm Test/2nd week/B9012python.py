import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
	dummyStack = []
	string = input()
	try:
		for c in string:
			if c == '(':
				dummyStack.append(c)
			elif c == ')':
				if dummyStack[-1] == '(':
					dummyStack.pop()
				else:
					print("NO")
					break
	except IndexError:
		print("NO")
		continue			
	
	if not dummyStack: print("YES")
	else: print("NO")

            
