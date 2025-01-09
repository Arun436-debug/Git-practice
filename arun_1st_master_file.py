
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
    