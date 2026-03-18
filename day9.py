#prime or not prime
'''def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "prime"
    return "Not prime"
n=int(input("Entrr a number:"))
print(prime(n))'''


#Fibonacci Series
'''def fibonacci(n):
    a=0
    b=1
    for i in range(n+1):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
fibonacci(7)'''

#Fibonacci sereies other type
'''def fibonacci_series(n):
    a=0
    b=1
    if n>=1:
        print(a,end=" ")
    if n>=2:
        print(b,end=" ")
    for i in range(3,n+1):
        next=a+b
        print(next,end=" ")
        a=b
        b=next
fibonacci_series(4)'''
