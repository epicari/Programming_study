#
# HackerRank Python - Leap day
#
#
# year = 1992 일 때, year%100 = 92가 나와서 에러가 나므로, bool로 캐스팅 해야 함



def is_leap(year):

    return (not(year%4) and (bool(year%100) or not(year%400)))

    #return (year%4 == 0 and (year%100 != 0 or year%400 == 0))


if __name__ == '__main__':
    year = int(input())

    print(is_leap(year))