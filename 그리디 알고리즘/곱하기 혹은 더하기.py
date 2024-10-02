"""
문제 설명: 각 자리가 숫자(0 부터 9)로만 이루어진 문자열 S가 주어졌을 떄, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를
확인하며 숫자 사잉 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단 + 보다 x 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

입력 조건: 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 20)
출력 조건: 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

입력 예시 1: 02984
출력 예시 1: 576

입력 예시 2: 567
출력 예시 2: 210
"""

# 내가 푼 방법
S = input()
result = 0

for i in range(0, len(S)):
    if int(S[i]) == 0 or int(S[i]) == 1:
        result += int(S[i])

    else:
        if result == 0:
            result = 1

        result *= int(S[i])

print(result)

# 문제 답안 예시
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num

    else:
        result *= num

print(result)