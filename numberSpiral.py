def main(t):
    while(t>0):
        a,b = map(int,input().split(" "))
        M = max(a,b)
        print((a-b)*(-1)**M+(M*M)-M+1)
        t = t - 1

if __name__ == "__main__":
    t = int(input())
    main(t)