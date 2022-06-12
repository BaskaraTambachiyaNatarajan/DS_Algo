#This code uses fibanocci series to search an item in a list with Time complexity O(nlogn)


def minimum(a,b):
    if a<=b:
        return a
    else:
        return b

def fibanocci_search(n,arr,x):
        offset=-1
        fib_2=0
        fib_1=1
        fib=fib_1+fib_2
        while (fib<n):
            fib_2=fib_1
            fib_1=fib
            fib=fib_2+fib_1

        while(fib_1>=1):
            i=minimum(offset+fib_2,n)
            if(arr[i]==x):
                return i+1
            elif(arr[i]<x):
                offset=i
                fib=fib_1
                fib_1=fib_2
                fib_2=fib-fib_1
            else:
                fib=fib_2
                fib_1=fib_1-fib_2
                fib_2=fib-fib_1
        return -1

# Code execution starts here
if __name__=='__main__':
    arr=[10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100,235]
    n = len(arr)-1
    x = 100
    res=fibanocci_search(n,arr,x)
    print("Result ->",res)