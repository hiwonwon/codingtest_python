#높이차가 1이고 그러한 칸의 길이가 L의 배수일때 1 높일 수 있음
# n<=100

n,l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def check(line):
    bridge = [False for _ in range(n)]

    for i in range(1,n):
        if abs(line[i-1] - line[i])>1:
            return False
        else:
            #오른쪽
            if (line[i-1]-line[i]) == 1:
                for j in range(l):
                    #그래프 밖으로 나가는 경우
                    if i+j>= n:
                        return False
                    if line[i]!=line[i+j]:
                        return False
                    if bridge[i+j] == True:
                        return False
                    if bridge[i+j] == False:
                        bridge[i+j] = True
            #왼쪽
            elif (line[i-1]-line[i])== -1:
                for j in range(l):
                    if i-1-j <0 :
                        return False
                    if line[i-1] != line[i-j-1]:
                        return False
                    if bridge[i-1-j] == True:
                        return False
                    if bridge[i-1-j] == False:
                        bridge[i-1-j] = True
    return True


ans = 0
#가로
for i in range(n):
    if check(graph[i]):
        ans += 1
#세로
for j in range(n):
    if check([graph[i][j] for i in range(n)]):
        ans += 1
print(ans)
