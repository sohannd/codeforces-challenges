t =int(input())
for i in range(t):

    s = input().strip()
    if s.count("Y") <= 1:
        print("YES")
    else:
        print("NO")
