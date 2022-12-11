# 가장 가까운 같은 글자
def solution(s):
    answer = []
    dic = dict()
    for i, l in enumerate(s):
        if dic.get(l) is not None:
            answer.append(i - dic.get(l))
        else:
            answer.append(-1)
        dic[l] = i
    return answer