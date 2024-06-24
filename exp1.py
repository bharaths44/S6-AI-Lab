from itertools import permutations
n=int(input("Enter value of n : "))
for perm in permutations([i for i in range(n)]):
    print(perm)
    count=0
    for i,j in enumerate(perm):
        for k,l in enumerate(perm):
            if i+j==k+l or i-j==k-l:
                count+=1
    print(perm)
    if count==n:
        for a in range(n):
            for b in range(n):
                print("|Q|" if perm[a]==b else "| |",end="")
            print()
        print("\n")
