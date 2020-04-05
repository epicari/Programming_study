#
# HackerRank Nested Lists
#

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
    print('\n'.join([a for a,b in sorted(students) if b == second_num]))