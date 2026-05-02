#find maximum and minimum number
'''def max_min(l):
    max=l[0]
    min=l[0]
    for i in l:
        if i>max:
            max=i
        elif i<min:
            min=i
    print("MAX=",max)
    print("MIN=",min)
    return
l=[4,8,1,5,2,0,5]
max_min(l)'''

# Swap two variables without a temp variable
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''


# Swap two variables with a temp variable
'''a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)'''

# Check if a number is palindrome
'''def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if rev==temp:
        print("palindrome")
    else:
        print("Not palindrome")
    return
n=int(input("Enter a number:"))
palindrome(n)'''


