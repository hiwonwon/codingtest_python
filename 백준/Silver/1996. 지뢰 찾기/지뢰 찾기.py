n = int(input())
li = [["#"] * (n + 2)]
li += [["#"] + list(input()) + ["#"] for i in range(n)]
li.append(["#"] * (n + 2)) # 주변을 다 #으로 둘러 인덱스 에러가 나지 않도록 함
 
 
#     ↖   ↑   ↗   ←  →  ↙  ↓  ↘
di = [-1, -1, -1, 0, 0, 1, 1, 1] # 8방 탐색
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
 
answer = []
for i in range(1, n + 1):
    temp = []
    for j in range(1, n + 1):
        total = 0
        if li[i][j] != ".": # 지뢰인 경우 temp에 *을 삽입
            temp.append("*")
        else:
            for k in range(8):
                # 8방향에 대해 .도 아니고 #도 아니면 숫자이므로 지뢰의 개수를 센다.
                if li[i + di[k]][j + dj[k]] != "." and li[i + di[k]][j + dj[k]] != "#":
                    total += int(li[i + di[k]][j + dj[k]])
            if total > 9: # 10 이상이면 M으로 치환
                total = "M"
            temp.append(str(total))
    answer.append(temp)
 
for i in answer:
    print("".join(i))