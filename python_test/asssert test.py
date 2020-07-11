#
# assert 가정문 테스트
#
#

def assert_test(t):
    try:    
        assert type(t) is int, 'not int'
        print('type is int')
    except AssertionError as error: #assert가 False 일 경우 작동
        print(error) #Output excepted AssertionError (not int)
    except Exception as error:
        return error

arr = list(map(float, input().split()))

for i in arr:
    assert_test(i)