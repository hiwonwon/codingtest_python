n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()

first=data[(n-1)]
second= data[(n-2)] #두번째로 큰수
sum =0

mok = m//k
nmg = m%k

sum= first*k*mok + second*nmg


print(sum)