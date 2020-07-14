def main(n):
    count = 1
    max_val = list()
    j = 1
    for i in range(0,len(n)):
        temp = n[i]
        j = i + 1
        if(j<len(n) and temp ==n[j]):
            count +=1
            max_val.append(count)
        else:
            count = 1
            max_val.append(count)
    print(max(max_val))

if __name__ == "__main__":
    n = str(input())
    main(n)    