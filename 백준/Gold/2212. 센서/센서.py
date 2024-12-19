N,K=int(input()),int(input())
arr=sorted(list(map(int,input().split())))
diff=sorted([arr[i+1]-arr[i]for i in range(N-1)],reverse=1)
print(sum(diff[K-1:]))