#
# 백준 12791
# 주의할 점: 리스트.append(리스트)는 2차원, 리스트 += 리스트는 1차원
#

dic = {
1967: ['DavidBowie'],
1969: ['SpaceOddity'],
1970: ['TheManWhoSoldTheWorld'],
1971: ['HunkyDory'],
1972: ['TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'],
1973: ['AladdinSane','PinUps'],
1974: ['DiamondDogs'],
1975: ['YoungAmericans'],
1976: ['StationToStation'],
1977: ['Low', 'Heroes'],
1979: ['Lodger'],
1980: ['ScaryMonstersAndSuperCreeps'],
1983: ['LetsDance'],
1984: ['Tonight'],
1987: ['NeverLetMeDown'],
1993: ['BlackTieWhiteNoise'],
1995: ['1.Outside'],
1997: ['Earthling'],
1999: ['Hours'],
2002: ['Heathen'],
2003: ['Reality'],
2013: ['TheNextDay'],
2016: ['BlackStar']}

q = int(input())
for _ in range(q):
    s, e = map(int, input().split())
    cnt = 0
    res = []
    for i in range(s, e+1):
        try:
            a = dic[i]
            cnt += len(dic[i])
            res += [[i, e] for e in a]
        except:
            pass
    print(cnt)
    for e in res:
        print(*e)