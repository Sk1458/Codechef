#program to print max number of the given two numbers


t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    print(max(X,Y))
