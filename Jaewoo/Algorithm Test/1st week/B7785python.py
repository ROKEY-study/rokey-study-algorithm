n = int(input())
logDict = {}
for i in range(n):
    record = list(input().split(' '))
    try:
        del logDict[record[0]]
    except Exception:
        logDict[record[0]]='enter'
keyList = list(logDict.keys())
keyList.sort(reverse=True)
for key in keyList:
    print(key)