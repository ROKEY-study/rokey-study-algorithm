n = int(input())
for i in range(n):
    k = int(input())
    clothesDict = {}
    for j in range(k):
        key = list(input().split(' '))[1]
        try:
            clothesDict[key] += 1
        except KeyError:
            clothesDict[key] = 1
    clothesNums = list(clothesDict.values())
    selectNum = 1
    for num in clothesNums:
        selectNum *= (num + 1)
    selectNum -= 1
    print(selectNum)