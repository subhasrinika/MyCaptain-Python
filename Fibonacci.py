fib=int(input("Enter the value of n until which the Fibonacci series you want to print :"))
a=0
b=1
sum=0
count=1
while(count<=fib):
    print(sum,end= ' ')
    count=count+1
    a=b
    b=sum
    sum=a+b
        
