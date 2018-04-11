#Question: https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
#for next N input - check command an perform list operation or method
result = []
for _ in range(N):
    command, *args = input().split()
    if len(args)>0:
        args = list(map(int, args))

    if command in 'insert':
        result.insert(args[0], args[1])
    elif command in 'print':
        print(result)
    elif command in 'remove':
        result.remove(args[0])
    elif command in 'append':
        result.append(args[0])
    elif command in 'sort':
        result.sort()
    elif command in 'pop':
        result.pop()
    elif command in 'reverse':
        result.reverse()
