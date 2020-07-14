def main(n):
    t = list(map(int,input().split(" "))) 
    a = n*(n+1)//2
    b = sum(t)
    c = a - b
    print(c)

if __name__ == "__main__":
    n = int(input())
    main(n)