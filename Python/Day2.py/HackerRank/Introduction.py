1- # Print "Hello World"
print("Hello World")


2- Python If-Else
if __name__ == '__main__':
    num = int(input().strip())
    
    if (num%2 != 0):
        print("Weird")
    elif (num>=2) and (num<=5):
        print("Not Weird")
    elif (num>=6) and (num<=20):
        print("Weird")
    elif num > 20:
        print("Not Weird")


3- Arithmamtic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


4- Python Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a//b
    print(c)
    d= a/b
    print(d)


5-Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        if i<n:
            a= i*i
            print(a)

6-Write a Function
def is_leap(year):
    leap = False  
    if (year%4==0):
        leap = True
    if (year%4==0) and (year%100==0):
        leap = False
    if (year%4==0) and (year%400==0):
        leap = True
    return leap
year = int(input())

7- Print Function
if __name__ == '__main__':
    n = int(input())
    
    numbers = ""
    for i in range(1, n+1):
        numbers=numbers+str(i)
    print(numbers)

8- Introduction to Sets
def average(array):
    # your code goes here
    array=set(array)
    return sum(array)/len(array)
if __name__ == '__main__':

9- Symmetric Differece
m = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
lis = sorted((a-b).union(b-a))
for item in lis:
    print(item)

