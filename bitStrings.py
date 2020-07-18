def main(n):
    result = 2**n
    print(result % (10**9+7))

if __name__ == "__main__":
    n = int(input())
    main(n)