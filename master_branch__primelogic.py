while True:
    num = int(input('Enter the number : '))
    i = 1
    cnt = 0
    while i<=num:
        if num%i == 0:
            cnt = cnt+1
        i = i+1
    if cnt == 2:
        print(num,' is prime number')
        print()
        
    else:
        print('Not a Prime number')
        print()

    
    s = 'Yy'
    k = input('do yo want to continue with this code Y/N ? : ')
    if k in s or k in s :
        continue
    else:
        print('The End - Thank you for using Prime Code')
        break
