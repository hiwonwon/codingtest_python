def LCS(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # DP 테이블 채우기
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이
    lcs_length = dp[len1][len2]
    
    # LCS 문자열 복원
    lcs = []
    i, j = len1, len2
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()  # 역순이므로 뒤집기

    print(lcs_length)
    if lcs_length > 0:
        print("".join(lcs))

# 예제 실행
s1 = input().strip()
s2 = input().strip()
LCS(s1, s2)
