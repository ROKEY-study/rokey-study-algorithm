from collections import deque

N, M = map(int, input().split()) 

graph = []
for _ in range(N):
    line = input().strip()
    graph.append([int(char) for char in line])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

distance = [[0] * M for _ in range(N)]

queue = deque()
queue.append((0, 0))
distance[0][0] = 1 

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1 and distance[ny][nx] == 0:
                distance[ny][nx] = distance[y][x] + 1
                queue.append((ny, nx))

print(distance[N - 1][M - 1])