# 2019 Kakao Blind Recruitment_오픈채팅방
def solution(record):
    answer = []
    actions = []
    dic = {}

    for event in record:
        info = event.split()
        action, id = info[0], info[1]
        if action == "Enter" or action == "Change":
            dic[id] = info[2]
        actions.append((action, id))

    for action in actions:
        if action[0] == "Enter":
            answer.append(f'{dic[action[1]]}님이 들어왔습니다.')
        elif action[0] == "Leave":
            answer.append(f'{dic[action[1]]}님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
                "Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
