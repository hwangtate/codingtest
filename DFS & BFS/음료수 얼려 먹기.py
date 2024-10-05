column, row = map(int, input().split())  # column 세로, row 가로

board = []

for i in range(column):
    small_row = list(map(int, input()))
    board.append(small_row)

count = 0

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= column or y <= -1 or y >= row:
        return False

    # 현재 노드를 방문하지 않았다면
    if board[x][y] == 0:
        board[x][y] = 1
        # 상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


for i in range(column):
    for j in range(row):
        if dfs(i, j) == True:
            count += 1

print(count)

"""
4 5
00110
00011
11111
00000
"""