def febonaci(n):
    if n== 0 or n==1:
        return n
    else: 
        return febonaci(n-1)+febonaci(n-2) 

n = int(input())
print(febonaci(n))




