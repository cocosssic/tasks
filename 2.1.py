x=int(input())
y=int(input())
z=int(input())
if x==z==y:
    print(3)
elif x==z!=y:
    print(2)
elif y==z!=x:
    print(2)
elif x==y!=z:
    print(2)
elif x!=z!=y:
    print(0)