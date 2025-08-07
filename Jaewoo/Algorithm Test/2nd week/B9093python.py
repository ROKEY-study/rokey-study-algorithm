import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    result = ""
    words = input().split()
    for word in words:
        dummyList = list(word)
        while dummyList:
            result += dummyList.pop()
        result += ' '
    print(result)
    