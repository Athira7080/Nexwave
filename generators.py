t1=(10,20,30)
t2=(i for i in range(10))
print('t1=',t1)
print('t2=',t2)
print('list(t2)=',list(t2))

print('-'*40)

l=[1,2,3,4]#100MB
def squares(m):
    res=[]
    for j in m:
        r=j*j
        res.append(r)
    return res
r1=squares(l)
for a in r1:
    print('a=',a)

print('-'*40)

#multiple yields are possible in a program
def gen_squares(N):
    for k in N:
        yield k*k#it wont create an object ,but will keep a track of all objects. When we ask, it will generate object
        #it also returns
    for l in N:
        yield l*l

r2=gen_squares(l)
for b in r2:
    print('b=',b)

print('r1=',r1)
print('r2=',list(r2))#generators displays only once,so u wont get an /p here
print('-'*40)

o/p:

"C:\Users\lab365\Desktop\Python programming\myvenv1\Scripts\python.exe" C:/Users/lab365/Desktop/python/bin/generators_ex.py
t1= (10, 20, 30)
t2= <generator object <genexpr> at 0x0000023787E107B0>
list(t2)= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
----------------------------------------
a= 1
a= 4
a= 9
a= 16
----------------------------------------
b= 1
b= 4
b= 9
b= 16
b= 1
b= 4
b= 9
b= 16
r1= [1, 4, 9, 16]
r2= []
----------------------------------------

Process finished with exit code 0
