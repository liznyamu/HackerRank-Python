#Question : https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))
    # create a list of lists        
    grades = list(map(list,zip(names, scores)))
    
    #sort in place the list of list bases on the scores - http://bit.ly/2uTKtdF
    grades.sort(key = lambda x: x[1]) # grades sorted by score
    
    #get grades above lowest grade grades[0][1])
    new_grades = list(filter(lambda x: x[1] > grades[0][1], grades))
    
    #get second lowest grades
    seconds = [x for x in new_grades if (x[1] == new_grades[0][1])] # using list comprehensions
    
    #print names with second lowest grade - in alphabetic order
    seconds.sort(key = lambda x: x[0])# grades sorted by name
    for second in seconds:
        print(second[0])
    
    

