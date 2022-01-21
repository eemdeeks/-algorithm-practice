def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = []
    bridge = []
    
    while True :
        if len(truck_weights) == 0:
            break
        answer += 1
        time = list(map(lambda x:x-1,time))

        if len(time) != 0 :
            if time[0]== 0:
                time.pop(0)
                bridge.pop(0)
            
        if (sum(bridge) + truck_weights[0])<= weight:
            bridge.append(truck_weights.pop(0))
            time.append(bridge_length)
        
    answer += bridge_length    

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length,weight,truck_weights))