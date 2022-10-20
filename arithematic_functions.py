#python arithmetic simple functions
def add(num1,num2):
    sum=num1+num2
    print(sum)

def sub(num1,num2):
    if(num2>num1):
        ans=num2-num1
        print(ans)
    else:
        ans=num1-num2
        print(ans)

    def multiply(num1,num2):
        product=num1*num2
        print(product)

    def divide(num1,num2):
        quotient=num2//num1
        print(quotient)

    def modulo(num1,num2):
        remainder=num2%num1
        print(remainder)

    #main()
    num1=int(input())
    num2=int(input())
    print('''Choices for arithemetic operations are:
    1.addition
    2.subtraction
    3.multiplication
    4.division
    5.remainder''')
    #please enter your choice:-
    c=int(input("Please enter the sequence number of the operation you want to need"))
    if (c==1):
        print(add(num1,num2))
    elif(c==2):
        print(sub(num1,num2))
    elif(c==3):
        print(multiply(num1,num2))
    elif(c==4):
        print(divide(num1,num2))
    else:
        print(modulo(num1,num2))

