"""
여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며,
시작 좌표는 항상(1,1)입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

L R U D 로 이동
"""

# 내가 구현한 방법
n = int(input())
plan = list(input().split())

position = [1, 1]
box = [n, n]

for i in plan:
    if i == "R":
        position[1] += 1
        if position[1] > box[1]:
            position[1] -= 1

    if i == "L":
        position[1] -= 1
        if position[1] < 1:
            position[1] += 1

    if i == "U":
        position[0] -= 1
        if position[0] < 1:
            position[0] += 1

    if i == "D":
        position[0] += 1
        if position[0] > box[0]:
            position[0] -= 1

print(position)

# 답안 예시
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    nx = 0
    ny = 0

    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)