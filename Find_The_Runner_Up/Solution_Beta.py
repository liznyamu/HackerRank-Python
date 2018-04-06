#Question : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    
    m = max(arr)
    arr = list(filter(lambda x: x < m, arr))
    print(max(arr))
    
   
    

