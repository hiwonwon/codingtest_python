from collections import deque
def solution(begin, target, words):
    answer = 0
    
    #알파벤 하나만 다른지 체크해주는 함수
    def check (a,b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt+=1
        if cnt == 1:
            return True
        else:
            return False
    
    def bfs(b,target,answer):
        q = deque()
        #begin 단어는 words에 없으므로 idx 값 0으로 삽입
        q.append((b,0))
        if target not in words:
            return 0
        visited = [0] * len(words)
        
        while(q):
            b,idx = q.popleft()
            if b == target:
                return visited[idx]
            for i in range(len(words)):
                #현재 글자와 하나만 다르고 방문한적 없는 글자이면
                    if check(b,words[i]) and visited[i] == 0:
                        q.append((words[i],i))
                        visited[i] = visited[idx] + 1
                        
                        
                        
                    
    answer = bfs(begin,target,answer)               
            
        
    
    return answer

    