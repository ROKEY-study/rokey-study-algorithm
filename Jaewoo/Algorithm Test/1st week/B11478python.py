string = input()
n = len(string)
setString = []
for i in range(0, n):
    for j in range(i+1, n+1):
        setString.append(string[i:j])
print(len(set(setString)))