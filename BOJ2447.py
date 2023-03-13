def star(N) :
    if N ==  3 :
        return ['***', '* *', '***']
    else :
        star_arr = star(N//3)
        a = []

        for i in star_arr :
            a.append(i*3)   # 전 패턴을 각각 3개씩 늘림

        for i in star_arr :
            a.append(i + " "*(N//3) + i)    # 공백 추가
        
        for i in star_arr :    # 1과 동일
            a.append(i*3)

        return a

N = int(input())
print("\n".join(star(N)))   # 줄 바꾸며 문자열 합체