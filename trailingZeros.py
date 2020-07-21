import math

def main(n):
    i = 5
    count=0
    while(n/i>=1):
        count += n//i
        i *=5 
    print(count)

if __name__ == "__main__":
    n = int(input()) 
    main(n)