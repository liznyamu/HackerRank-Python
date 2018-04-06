#Question : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    
    list_runners = list(set(arr))
    list_runners.sort()
    print(list_runners[-2])
    
    

