from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    current_w = 0
    while(truck_weights):
        answer += 1
        #다리의 마지막지점에 있던 트럭을 빼줌
        current_w -= bridge.pop(0)
        
        #현재 트럭 더해도 최대 무게 넘지 않을 때
        if current_w + truck_weights[0] <= weight:
            current_w += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        
    #마지막 트럭이 다리를 건너는데 필요한 시간        
    answer += bridge_length 
    return answer