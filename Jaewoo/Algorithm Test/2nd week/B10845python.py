import sys
input = sys.stdin.readline

n = int(input())
dummyStack = []
for i in range(n):
	commands = input().split()
	if commands[0] == 'push': dummyStack.append(int(commands[1]))
	elif commands[0] == 'pop': 
		if not dummyStack:
			print(-1)
		else:
			print(dummyStack.pop(0))
	elif commands[0] == 'size': print(len(dummyStack))
	elif commands[0] == 'empty': print(int(not dummyStack))
	elif commands[0] == 'front':
		if not dummyStack:
			print(-1)
		else:
			print(dummyStack[0])
	elif commands[0] == 'back':
		if not dummyStack:
			print(-1)
		else:
			print(dummyStack[-1])
