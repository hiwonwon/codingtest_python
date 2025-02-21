import sys
sys.setrecursionlimit(10**6) # 최대 재귀 회수 확장

array=[]
while True:
    try:
        array.append(int(input()))
    except:
        break
    
def dfs(start,end):
    if start > end: # 오른쪽 자식 노드가 없는 경우 =>리프 노드인 경우우
        return
    right_start=end+1 # 오른쪽 노드가 없을 경우 대비해서 종료 조건 설정
    
    for i in range(start+1,end+1): # 서브 트리에서 루트 노드를 제외한 자식 노드 중에서 루트 노드 보다 큰 값을 찾음
        if array[start]<array[i]:
            right_start=i
            break
    
    dfs(start+1,right_start-1) # 왼쪽 서브 트리 
    dfs(right_start,end) # 오른쪽 서브 트리
    print(array[start])
        
    
dfs(0,len(array)-1)