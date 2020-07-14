from collections import deque

def main(n):
    a = [int(i) for i in range(1,(n//2))]
    print(n)
    b = [int(j) for j in range(n,(n//2)+1)]
    print(a)
    print(b)
    temp = sum(a)//2
    if(n%4==0 or n%4==3):
        print("YES")
    else:
        print("NO")
    

if __name__ == "__main__":
    n = int(input())
    main(n)