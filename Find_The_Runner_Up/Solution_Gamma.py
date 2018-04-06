#Question : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]    
    m = max(arr)
    
    #check if all values are the max value
    if arr.count(m) == len(arr):
        print(m)
    else: 
        while max(arr) == m: #remove all instances on max value without using 'set'
            arr.remove(m) 
        print(max(arr))
    
    
   
    

