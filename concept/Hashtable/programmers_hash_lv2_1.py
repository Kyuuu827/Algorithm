# 전화번호 목록_lv2
def solution(phone_book):
    answer = True
    phone_dic = {}

    for phone_number in phone_book:
        phone_dic[phone_number] = 0

    for phone_number in phone_book:
        temp = ''
        for num in phone_number:
            temp += num
            if temp in phone_dic and temp != phone_number:
                return False
    return answer

print(solution(["119", "97674223", "1195524421"]))