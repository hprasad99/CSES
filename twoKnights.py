def main(n):
    for i in range(1,n+1):
        ans = ((i**2)*((i**2)-1)//2)-(4*(i-1)*(i-2))
        print(ans)

if __name__ == "__main__":
    n = int(input())
    main(n)