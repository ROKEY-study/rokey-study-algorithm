n = int(input())
dummyStack = []
for i in range(n):
	commands = input().split()
	if commands[0] == 'push': dummyStack.append(int(commands[1]))
	if commands[0] == 'pop': 
		if not dummyStack:
			print(-1)
		else:
			print(dummyStack.pop())
	if commands[0] == 'size': print(len(dummyStack))
	if commands[0] == 'empty': print(int(not dummyStack))
	if commands[0] == 'top':
		if not dummyStack:
			print(-1)
		else:
			print(dummyStack[-1])
