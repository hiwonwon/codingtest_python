#동 -> 동북서남
#서 -> 서남동북
#남 -> 남동북서
#북 -> 북서남동
# 재귀
# for문 안에서 좌표 전진가능하면(0) cnt += 1
# 종료 조건 : 전역변수 flag가 True 일 때. for문 모두 (1) 이면 전역 변수 flag 종료로 만듦

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

cnt = 0
E = (0,1)
W = (0,-1)
S = (1,0)
N = (-1,0)
direction_dict = {0:[W,S,E,N], 1:[N,W,S,E], 2:[E,N,W,S], 3:[S,E,N,W]}
dir_num = {N:0, E:1, S:2, W:3}

def clean(i,j,d):
    global cnt
    # global stop
    # if stop:
    #     return
    if maps[i][j] == 0:
        cnt += 1
        maps[i][j] = -1
        
    dirs = direction_dict[d] #방향 우선순위 배열
    
    for dir in dirs:
        r = dir[0]
        c = dir[1]
        if maps[i+r][j+c] == 0: #청소 안된 경우
            new_d = dir_num[dir]
            clean(i+r, j+c, new_d)
            return
    #4방향 모두 청소됐을 때      
    r,c = dirs[-1] 
    r, c = r*(-1), c*(-1) #후진 좌표
    
    if maps[i+r][j+c] != 1: #벽이 아닐 때
    #     print("후진")
        clean(i+r, j+c, d)
        return
            
n, m = map(int,input().rstrip().split())

r, c, d = map(int,input().rstrip().split())

maps = []
for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))
    
clean(r,c,d)
print(cnt)