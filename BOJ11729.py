def hanoi (n, a, b, c) :
    # 원판이 하나일 경우는 장대1(a)에서 장대3(c)으로 그냥 옮기면 끝
    if n == 1 :
        print(a, c)
    else :
        # 원판 n-1개를 장대1(a)에서 장대2(b)으로 옮김 
        hanoi(n-1, a, c, b)
        # n번째 원반, 즉 제일 밑에 있는 원판을 장대3(c)으로 옮김
        print(a, c)
        # 장대2(b)에 있는 원반 n-1개를 장대3(c)으로 옮김
        hanoi(n-1, b, a, c)

n = int(input())
# 옮긴 횟수
print(2**n-1)
# 옮기는 과정
hanoi(n, 1, 2, 3)