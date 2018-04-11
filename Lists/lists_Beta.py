#Question: https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
#for next N input - check command an perform list operation or method
result = []
for _ in range(N):
    command, *args = input().split()

    if command not in 'print':
        command = command + '(' + ','.join(args) + ')'
        eval("result." + command)
    else:
        print(result)
