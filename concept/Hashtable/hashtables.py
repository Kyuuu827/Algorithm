# hash table(empty)
hash_table = list([0 for i in range(10)])

# 해시 함수 (Division 방식: 나머지 값 사용)
def hash_func(key):
    return key % 5

def hashtable_data(data, value):
    key = ord(data[0])
    hashed_key = hash_func(key)
    hash_table[hashed_key] = value

hashtable_data('Chankyu', 'lck0827@gmail.com')
hashtable_data('Tom', 'tom@gmail.com')
hashtable_data('James', 'James@gmail.com')

print(hash_table)

# open hashing
hash_table = list([0 for i in range(10)])

def get_key(data):    #해쉬 키 생성
    return hash(data)

def hash_func(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    # 해쉬 충돌이 발생할 경우(해쉬 주소가 동일할 경우)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            # Key가 동일하면 데이터를 덮어씀
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
                return 
        # Key가 동일하지 않으면 데이터를 연결해 저장함
        hash_table[hash_address].append([index_key, value])
    # 2. 해쉬 충돌이 발생하지 않으면 해당 버킷에 데이터 저장
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

save_data('Chankyu', 'lck0827@gmail.com')
save_data('Tom', 'Tom@gmail.com')
save_data('James', 'James@gmail.com')
print(read_data('Chankyu'))

#close hashing
hash_table = list([0 for i in range(10)]) # 빈 해쉬 테이블 생성

def get_key(data):     # 해쉬 키 생성
    return hash(data)

def hash_func(key):    # 간단한 해쉬 함수
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    
    # 해쉬 충돌이 발생할 경우(해쉬 주소가 동일한 경우)
    if hash_table[hash_address] != 0:
        # 충돌 일어난 위치부터 끝까지 스캔
        for index in range(hash_address, len(hash_table)):
        # 동일한 key 일 경우 덮어쓰기
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            # 빈 공간 찾으면 저장
            elif hash_table[index][0] == index_key: 
                hash_table[index][1] = value
    # 충돌 없으면 데이터 바로 저장
    else:
        hash_table[hash_address] = [index_key, value]
        
# 해쉬 데이터 조회
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

print(hash('Chankyu'))