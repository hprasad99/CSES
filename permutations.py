def main(n):
    a = [int(n) for n in range(1,n+1)]
    #print(a)
    if(n==2 or n==3):
        print("NO SOLUTION")
    else:
        for j in range(1,n,2):
            if(j<n):
                print(a[j],end=" ")    
        for i in range(0,n,2):
            if(i<n):
                print(a[i],end=" ")

if __name__ == "__main__":
    n = int(input())
    main(n)