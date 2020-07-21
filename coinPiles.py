def main(t):
    while(t):
        a,b = map(int,input().split(" "))
        if(2*a-b>=0 and (2*b-a)%3==0 and 2*b-a>=0 and (2*b-a)%3==0):
            print("YES")
        else:
            print("NO")
        t = t - 1 

if __name__ == "__main__":
    t = int(input())
    main(t)