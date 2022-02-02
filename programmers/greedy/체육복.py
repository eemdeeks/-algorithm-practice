def solution(n, lost, reserve):
    lost.sort()
    l = len(lost)
    ls = []
    for i in lost:
        if reserve.count(i)==1:
            reserve.remove(i)
            ls.append(i)
            l -= 1
    for i in ls:
        lost.remove(i)
    for i in lost:
        if reserve.count(i-1)==1:
            reserve.remove(i-1)
            l -= 1
        elif reserve.count(i+1)==1:
            reserve.remove(i+1)
            l -= 1
    answer = n - l
    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]

solution(n,lost,reserve)