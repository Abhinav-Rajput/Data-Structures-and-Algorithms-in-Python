def NGE(a):
    for i in range(0,len(a)):
        flag = 0
        nge =-1
        for j in range(i,len(a)):
            if a[j]>a[i]:
                flag =1
                nge = a[j]
                break
        if flag == 1:
            print(a[i],nge)
        else:
            print(a[i],nge)

def main():
    a= [4,5,2,25]
    NGE(a)

if __name__ == '__main__':
    main()            
