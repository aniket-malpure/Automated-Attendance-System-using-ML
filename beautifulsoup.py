def angryProfessor():
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))
        sum=0
        for i in a:
            if i<0:
                sum=sum+1
            if i == 0:
                sum=sum+1
            if sum>k:
                print("NO")
            else:
                print("YES")
result = angryProfessor()
