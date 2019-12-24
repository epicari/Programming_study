#
# HackerRank Nested Lists
#
# 낮은 점수 찾기 ... 검색을 위해 score 따로 저장해야?
# ㄴ second_num에 두번째로 낮은 점수 저장
# ㄴ sorted는 리스트 정렬 후 반환까지 함, sort는 정렬만 시킴
# 원하는 점수를 가진 리스트 위치를 반환 받은 다음, 반환 받은 위치를 출력? index()
# ㄴ index로 못 찾음 2차원 리스트라 그런가 봄
# ㄴ 

if __name__ == "__main__":
    students = []
    scoreSet = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scoreSet.add(score)

    #second_num = min([x for x in scoreSet if x != min(scoreSet)])

    second_num = sorted(scoreSet)[1]
    print('\n'.join([a for a,b in sorted(students) if b == second_num])) #이게 students[a][b] 인 듯