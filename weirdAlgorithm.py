def main(n):
    temp = n
    while(n!=1):
        print(int(n),end=" ")
        if(n%2==0):
            n = n/2
        else:
            n=n*3+1
    print( 1)
    
if __name__ == "__main__":
    n = int(input())
    main(n)