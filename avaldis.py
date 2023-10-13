A, B = [int(a) for a in input().split(" ")]

if A == 0:
    print(str(B))
elif A == 1:
    if B == 0:
        print("x")
    elif B > 0:
        print("x+" + str(B))
    else:
        print("x" + str(B))
elif A == -1:
    if B == 0:
        print("-x")
    elif B > 0:
        print("-x+" + str(B))
    else:
        print("-x" + str(B))
else:
    if B == 0:
        print(str(A) + "x")
    elif B > 0:
        print(str(A) + "x+" + str(B))
    else:
        print(str(A) + "x" + str(B))