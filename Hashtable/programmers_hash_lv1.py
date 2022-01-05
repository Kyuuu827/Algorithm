# 프로그래머스_해시_완주하지 못한 선수
def solution(participant, completion):
    marathon_dic= {}
    for i in participant:
        marathon_dic[i] = "fail"
    for j in completion:
        marathon_dic[j] = "success"
    for key, value in marathon_dic.items():
        if value == "fail":
            return key  # 동명이인이 없을 경우엔 가능한 로직이지만, 동명이인을 판별하지 못한다. 

# 수정 코드 -> 정답
def solution(participant, completion):
    marathon_dic = dict()
    hashValue = 0
    
    for player in participant:
        marathon_dic[hash(player)] = player
        hashValue += hash(player)

    for finisher in completion:
        hashValue -= hash(finisher)
        
    return marathon_dic[hashValue]
