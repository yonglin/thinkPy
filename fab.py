def fab(n):
    if n == 0 or n== 1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
    
print fab(10)
