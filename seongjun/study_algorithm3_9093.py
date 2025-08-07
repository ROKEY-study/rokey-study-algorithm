# 문제
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

# 예제 입력 1
# 2
# I am happy today
# We want to win the first prize
# 예제 출력 1
# I ma yppah yadot
# eW tnaw ot niw eht tsrif ezirp


text = "I am happy today"
text_list = text.split()  #
result = []
for i in range(len(text_list)):
    temp1 = list(text_list[i])
    temp2 = []
    for _ in range(len(text_list[i])):
        char = temp1.pop()
        temp2.append(char)
    result.append(temp2)
print(result)
result2 = []
for j in range(len(result)):
    result2.append("".join(result[j]))
print(result2)
result3 = " ".join(result2)
print(result3)


text = "I am happy today"
words = text.split()

# 한 줄로 단어 뒤집기 리스트 만들기
reversed_words = [word[::-1] for word in words]

# 리스트를 문자열로 합치기
result = " ".join(reversed_words)

print(reversed_words)  # ['I', 'ma', 'yppah', 'yadot']
print(result)  # I ma yppah yadot
