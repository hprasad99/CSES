def main(n,key):
    low = 0
    high = len(n)-1
    while(low<high):
        mid = (low+high)//2
        if(n[mid]<key):
            low = mid + 1
        elif(n[mid]>key):
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    n = str(input())
    key = str(input())
    pos = main(n,key)
    print(pos)