from itertools import permutations

n = int(input())
k = int(input())

nums = []
for i in range(n):
    nums.append(input())

numList = []
for idxList in permutations(range(n), k):
    dummyStr = ""
    for i in idxList:
        dummyStr += nums[i]
    numList.append(dummyStr)

print(len(set(numList)))
