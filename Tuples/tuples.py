#Question: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) #map returns an iterator of type map
    t = tuple(integer_list)
    print(hash(t))
