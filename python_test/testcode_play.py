n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    l = input().split()
    argv = set(map(int, input().split()))   
    cmd = l[0] + "(" + str(argv) + ")"
    eval("s.{0}".format(cmd))
print(sum(s))