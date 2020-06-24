#
# 철자바꾸기
# 기준을 뽑고 기준과 똑같으면 철자를 바꾼 것이라고 판단
# 
#

#text = ['code', 'doce', 'ecod', 'framer', 'frame'] #code, framer, frame
text = ['code', 'anagram', 'doce', 'aaagrnm'] #code, anagram

text.sort()
res = []
s = text[0]
for i in range(1, len(text)):
    if len(s) == len(text[i]):
        if sorted(s) == sorted(text[i]):
            res.append(s)
    else:
        res.append(text[i])
        s = text[i]
for i in set(res):
    print(i)