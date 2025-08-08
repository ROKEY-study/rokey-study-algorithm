# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
from collections import defaultdict

computers = int(input())
N = int(input())
network = defaultdict(list)

for i in range(N):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)

stack = [1]
visited = set()

while stack:
    node = stack.pop()
    if node not in visited:
        stack.extend(network[node])
        visited.add(node)

print(len(visited) - 1)