from collections import deque
def solution(begin, target, words):
    answer = 0
    #변환할 수 없는 경우
    if target not in words:
        return answer
    
    return bfs(begin, target, words)
    
def bfs(begin, target, words):
    
        q = deque()
        q.append([begin,0])
        
        while(q):
            now, step = q.popleft()
            
            if now == target:
                return step
            
            for word in words:
                cnt = 0
                for i in range(len(word)):
                    if word[i] != now[i]:
                        cnt += 1
                        
                if cnt == 1:
                    q.append([word,step+1])