#from collections import deque

def main(n):
    v1 = list()
    v2 = list()
    if(n*(n+1)//2==0):
        print("NO")
        exit
    if(n%4==0):
        j=3
    else:
        j=4
    i=0
    while(i<(n-1)//4):
        v1.append(4*i+1+j)
        v1.append(4*i+4+j)
        v1.append(4*i+2+j)
        v1.append(4*i+3+j)
        i = i + 1
    if(n%4):
        v1.append(1)
        v1.append(2)
        v1.append(3)
    else:
        v1.append(1)
        v1.append(4)
        v1.append(3)
        v1.append(2)
    print("YES\n")
    print(len(v1),"\n")
    for i in range(0,len(v1)):
        print(v1[i],end=" ")
    print()
    print(len(v2),"\n")
    for i in range(0,len(v2)):
        print(v2[i],end=" ")

if __name__ == "__main__":
    n = int(input())
    main(n)