#Question : https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    marks = []
    for _ in range(int(input())):
        marks.append([input(), float(input())])
    #print(marks)
    
    #get second lowest grade
    second_lowest = sorted(list(set([mark[1] for mark in marks])))[1]
    #print(second_lowest)
    
    #print names with second lowest grade in alphabetical order
    #print(sorted(marks))
    print('\n'.join([name for name, score in sorted(marks) if score == second_lowest]))
    
    
    

