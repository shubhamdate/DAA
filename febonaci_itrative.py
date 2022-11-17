def febonaci(n):
    if n== 0 or n==1:
        return n
    else: 
        i= 0
        num1 = 0
        num2 = 1
        while(i < n-1):
            i+=1
            sum= num1+num2
            num1= num2
            num2=sum
    return sum

n = int(input())
print(febonaci(n))