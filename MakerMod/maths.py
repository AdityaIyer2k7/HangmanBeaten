def Sum(values):
    n = 0
    for value in values:
        n = n + value
    return n

def Multiply(numbers):
    n = 1
    for value in numbers:
        n = n*value
    return n

def Divide(numerator,denominator):
    n = numerator/denominator
    return n

def Power(base,power):
    n = 1
    for i in range(0,power):
        n = n*base
    return n

def Mean(numbers):
    values = 0
    n=0
    for number in numbers:
        n = n + number
        values = values+1
    answer = n/values
    return answer

def Median(numbers):
    numbers.sort()
    values = 0
    for number in numbers:
        values = values+1
    oddEven = values%2
    if oddEven == 1:
        idx = values-1
        idx = idx/2
        n = numbers[int(idx)]
    else:
        a = int(values/2)
        valA = numbers[a-1]
        valB = numbers[a]
        n = Mean([valA,valB])
    return n

def isPrime(num):
    if num <= 2:
        result="guess yourself"
    for i in range(2,num):
        if num%i == 0:
            result="n"
            break
        else:
            result="y"
    return result

def HCF(num1,num2):
    #Also known as GCD
    if num1>num2:
        n1=num1
        n2=num2
    elif num1<num2:
        n1=num2
        n2=num1
    else:
        n1=num1
        n2=num2
    while True:
        m=n1%n2
        if m==0:
            r=n2
            break
        else:
            pass
        n1=n2
        n2=m
    return r

def LCM(num1,num2):
    r=(num1*num2)/HCF(num1,num2)
    return r
