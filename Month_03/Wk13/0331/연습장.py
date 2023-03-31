def rotated_90degree(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock):
    length_lock = len(new_lock) // 3
    for i in range(length_lock, length_lock * 2):
        for j in range(length_lock, length_lock * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 3배 계왕권
    new_lock = [[0] * (n *3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] += lock[i][j]
        
    for rotate in range(4): # key를 돌려보자
        key = rotated_90degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        if check(new_lock) == True:
                            return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False
