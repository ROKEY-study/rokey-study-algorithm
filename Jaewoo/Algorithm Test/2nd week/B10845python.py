import sys
input = sys.stdin.readline

n = int(input())
dummyQueue = []
for i in range(n):
	commands = input().split()
	if commands[0] == 'push': dummyQueue.append(int(commands[1]))
	elif commands[0] == 'pop': 
		if not dummyQueue:
			print(-1)
		else:
			print(dummyQueue.pop(0))
	elif commands[0] == 'size': print(len(dummyQueue))
	elif commands[0] == 'empty': print(int(not dummyQueue))
	elif commands[0] == 'front':
		if not dummyQueue:
			print(-1)
		else:
			print(dummyQueue[0])
	elif commands[0] == 'back':
		if not dummyQueue:
			print(-1)
		else:
			print(dummyQueue[-1])