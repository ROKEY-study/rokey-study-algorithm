# 9
# 7 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6

from collections import defaultdict, deque

relationship = defaultdict(list)

n = int(input())
person1, person2 = map(int, input().split())

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    relationship[x].append(y)
    relationship[y].append(x)

queue = deque()
visited = set()
found = False

queue.append((person1, 0))

while queue:
    node, distance = queue.popleft()

    if node == person2:
        found = True
        print(distance)
        break

    for neighbor in relationship[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, distance + 1))

if not found:
    print(-1)