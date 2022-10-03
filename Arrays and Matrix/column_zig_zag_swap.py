#!/usr/bin/env python
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
mod=[]
for i in zip(*mat):
    mod.append(list(i))
l=[]
for i in range(c):
    if i%2==0:
        l.append(list(mod[c-1-i][r//2:]+mod[i][r//2:]))
    else:
        l.append(list(mod[i][:r//2]+mod[c-1-i][:r//2]))
for i in zip(*l):
    print(*i)
