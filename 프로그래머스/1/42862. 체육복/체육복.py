def solution(n, lost, reserve):
    answer = 0
    nlost = [l for l in lost if l not in reserve]
    nreserve = [r for r in reserve if r not in lost]
    nlost.sort()
    nreserve.sort()
    
    for r in nreserve:
        m = r-1
        p = r+1
        
        if m in nlost:
            nlost.remove(m)
        elif p in nlost:
            nlost.remove(p)
    
    return n - len(nlost)