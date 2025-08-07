n = int(input())
class Stack:
	def __init__(self):
		self.data = []
	def push(self,datum):
		self.data.append(int(datum))
	def pop(self):
		if not self.data:
			print(-1)
		else:
			print(self.data.pop())
	def size(self):
		print(self.data.__len__())
	def empty(self):
		print(int(not self.data))
	def top(self):
		if not self.data:
			print(-1)
		else:
			print(self.data[-1])

stack = Stack()
for _ in range(n):
	command = input().split()
	func = getattr(stack,command[0])
	if command[0] == "push":
		func(command[1])
	else:
		func()

