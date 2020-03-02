def swap(s):
    result = ''
    for i in s:
        if i.isupper():
            result += (i.lower())
        else:
            result += (i.upper())
    return result

s = 'Www.HackerRank.Com'
print(swap(s))