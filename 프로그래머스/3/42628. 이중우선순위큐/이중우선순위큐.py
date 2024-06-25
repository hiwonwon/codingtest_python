import heapq

def solution(operations):
    answer = [0,0]
    hq = []
    
    def i(x):
        heapq.heappush(hq,x)
        
    def d():
        del hq[-1]
    def d_1():
        del hq[0]
            
    for o in operations:
        tmp = o.split()
        
        if tmp[0] == 'I':
            i(int(tmp[1]))
        elif tmp[0] == 'D':
            if len(hq)!= 0 :
                if tmp[1] == '-1':
                    d_1()
                else:
                    d()
            else:
                continue
                    
    
    if len(hq)>0:
        answer[0] = max(hq)
        answer[1] = min(hq)
        
    return answer