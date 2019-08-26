argc, argv = map(int, input('숫자 입력: ').split())
print(max(int(str(argc)[::-1]), int(str(argv)[::-1])))