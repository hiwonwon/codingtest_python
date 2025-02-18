from collections import deque
t = int(input())

def L(n):
    d1 = n // 1000
    d2 = n //100 % 10
    d3 = n // 10 % 10
    d4 = n % 10

    q = deque([d1,d2,d3,d4])
    q.rotate(-1)
    tmp = ''
    for qq in q:
        tmp += str(qq)
    return(int(tmp))


def R(n):
    d1 = n // 1000
    d2 = n //100 % 10
    d3 = n // 10 % 10
    d4 = n % 10

    q = deque([d1,d2,d3,d4])
    q.rotate(1)
    tmp = ''
    for qq in q:
        tmp += str(qq)
    return(int(tmp))

def bfs(a,b):
    q = deque()
    q.append([a,''])
    visited = [0] * (10000)
    visited[a] = 1

    while(q):
        now, ans = q.popleft()
        if now == b :
            print(ans)
            break
        d = now * 2 % 10000
        if not visited[d]:
            visited[d] = 1
            q.append([d,ans+'D'])

        s = (now - 1) % 10000
        if not visited[s]:
            q.append([s,ans+'S'])
            visited[s] = 1

        l = now//1000 + now%1000 *10
        if not visited[l]:
            q.append([l,ans+'L'])
            visited[l] = 1

        r = now%10 * 1000 + now//10
        if not visited[r]:
            q.append([r,ans+'R'])
            visited[r] = 1
        



for _ in range(t):
    a,b = map(int,input().split())
    bfs(a,b)

