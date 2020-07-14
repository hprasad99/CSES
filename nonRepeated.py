def main(n):
    non = [0]*26
    offset = ord('a')
    for i in range(0,len(n)):
        non[ord(i)-offset]+=1
    print(non)

if __name__ == "__main__":
    n = str(input())
    main(n)