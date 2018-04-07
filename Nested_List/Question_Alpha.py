#Question : https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))
    # create a list of lists        
    grades = list(map(list,zip(names, scores)))
    #print(grades)
    #sort in place the list of list bases on the scores - http://bit.ly/2uTKtdF
    grades.sort(key = lambda x: x[1]) # grades sorted by score

    #get grades above lowest grade grades[0][1])
    above_lowest = list(filter(lambda x: x[1] > grades[0][1], grades))
    seconds = list(filter(lambda x: x[1] == above_lowest[0][1], above_lowest))
    seconds.sort(key = lambda x: x[0])# grades sorted by name
    for second in seconds:
        print(second[0])
    
    

