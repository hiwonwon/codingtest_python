import copy

n, m = map(int,input().split())
cctv = []
board = []
for i in range(n):
        data = list(map(int,input().split()))
        board.append(data)
        for j in range(m):
            if 1<= data[j] <= 5:
                 cctv.append([data[j],i,j])


#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 감시해야하는 모든 방향 (각각의 cctv별로 감시할 수 있는 방향)
mode = [
     [],
     [[0],[1],[2],[3]],
     [[0,2],[1,3]],
     [[0,1],[1,2],[2,3],[0,3]],
     [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
     [[0,1,2,3]],
]


def fill(board,mode,x,y):
    for i in mode:
         nx = x
         ny = y
         while True:
              nx += dx[i]
              ny += dy[i]
              if nx<0 or ny<0 or nx>=n or ny>=m:
                   break
              if board[nx][ny] == 6:
                break
              elif board[nx][ny] == 0:
                  board[nx][ny] = -1
                   
         

def backtacking(cnt,graph):
    global ans
    #전부 탐색 완료한 경우
    if cnt == len(cctv):
        count = 0
        for i in range(n):
            count += graph[i].count(0)
        #최소 사각지대 개수 업데이트
        ans = min(count,ans)
        return
    
    tmp = copy.deepcopy(graph)
    ccty_type, x, y = cctv[cnt]
    for i in mode[ccty_type]:
         fill(tmp,i,x,y)
         backtacking(cnt+1,tmp)
         tmp = copy.deepcopy(graph)
    

ans = int(1e9)
backtacking(0,board)
print(ans)