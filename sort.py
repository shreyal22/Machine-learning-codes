def klar(arr,k):
    arr.sort(reverse=True)
    
    return arr[k-1]
if __name__=='__main__':
 arr=[2,3,4,59,6,7,8]
 k=3
 print(klar(arr,k))