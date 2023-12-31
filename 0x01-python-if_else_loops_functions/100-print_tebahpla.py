for i in range(ord('z'), ord('a') - 1, -1):
    char = chr(i)
    case = char.upper() if i % 2 == 0 else char.lower()
    print("{}{}".format(case, char), end='')

