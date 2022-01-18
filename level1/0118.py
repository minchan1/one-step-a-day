# https://programmers.co.kr/learn/courses/30/lessons/12915
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
# 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
# 예를 들어 strings가 ["sun", "bed", "car"]이고 
# n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    c = []
    for i in range(len(strings)):
        b = ''.join(strings[i][n] + strings[i])
        c.append(b)
    c = sorted(c)
    for i in range(len(c)):
        c[i] = c[i][1:]
    return c


a = ["sun", "bed", "car"]
c = []
for i in range(len(a)):
    b = ''.join(a[i][1] + a[i])
    c.append(b)
c = sorted(c)
for i in range(len(c)):
    c[i] = c[i][1:]
print(c)
