n = int(input())
m = int(input())
if m == 0:
    print(min(abs(n-100), len(str(n))))
else:
    tmp = list(map(int, input().split()))
    l = []
    for i in range(10):
        if i not in tmp:
            l.append(i)
    if len(l)==1:
        length = len(str(n))
        m = abs(100-n)
        for i in range(1,length+2):
            m = min(m, abs(n-l[0]*((10**i-1)//9))+i)
        print(m)
    elif len(l)==0:
        print(abs(n-100))
    else:
        length = len(str(n))
        cand = []
        if length != 1:
            cand.append(abs(n-l[-1]*((10**(length-1)-1)//9))+length-1)
        def cal(x,t):
            if t == 0:
                cand.append(abs(n-x)+length)
                return
            for i in l:
                cal(10*x+i, t-1)
            return
        cal(0, length)
        if l[0]==0:
            cand.append(abs(n-l[1]*(10**length))+length+1)
        else:
            t = l[0]
            cand.append(abs(n-t*((10**(length+1)-1)//9))+length+1)
        cand.append(abs(n-100))
        print(min(cand))