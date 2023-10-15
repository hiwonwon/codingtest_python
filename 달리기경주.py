
def solution(players, callings):
    answer = []
    dic = {string : i for i,string in enumerate(players)}

    for i in range(len(callings)):
        idx = dic[callings[i]]
        # print(idx, players[idx] ,players[idx-1] )
        dic[players[idx]]=idx-1
        dic[players[idx-1]]=idx
        players[idx],players[idx-1]= players[idx-1],players[idx]
    answer =players
    return answer

players =input()
callings=input()

players = players.split()
players = [word.strip('[]",') for word in players]
callings = callings.split()
callings = [word.strip('[]",') for word in callings]

# for i in range(len(players)):
#     print(players[i])

print(solution(players,callings))