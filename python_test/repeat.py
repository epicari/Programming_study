def test(n, s):
    result = []
    for i in s:
        result.append(i*n)
    return print(''.join(result))

i_int = int(input('숫자 입력: '))
i_str = input('문자 입력: ')
test(i_int, i_str)