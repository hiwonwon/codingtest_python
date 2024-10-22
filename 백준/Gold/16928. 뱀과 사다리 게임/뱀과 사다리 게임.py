from collections import deque
n, m = map(int, input().split())
board = [[0] * 10 for _ in range(10)]
#사다리와 뱀을 저장하는 배열
ss = [[0] * 10 for _ in range(10)]

for _ in range(n):
    x, y = map(int, input().split())
    x-=1
    y-=1
    i = x // 10
    j = x % 10
    ss[i][j] = y
for _ in range(m):
    x, y = map(int, input().split())
    #0~99로 바꾸어줌
    x-=1
    y-=1
    i = x // 10
    j = x % 10
    ss[i][j] = y

def bfs(board,ss):
    q = deque()
    q.append((0,0))
    #board[0][0] = 1

    while(q):
        a,b = q.popleft()
        x = 10 * a + b
        for i in range(1,7):
            #nxt는 주사위를 굴려서 갈 다음 칸
            nxt = x+i
            u = nxt // 10
            v = nxt % 10
            if 0<=u<10 and 0<=v<10:
                #사다리나 뱀이 있는 칸이라면
                if ss[u][v] != 0:
                    #이동해야되는 칸의 정보 nxt에 저장
                    nxt = ss[u][v]
                    u = nxt // 10
                    v = nxt % 10
                #nxt칸이 아직 방문한 적 없고 범위내에 있다면 
                if 0<=u<10 and 0<=v<10 and board[u][v] == 0:
                    board[u][v] = board[a][b] + 1
                    q.append((u,v))

bfs(board,ss)
#print(ss)
print(board[9][9])