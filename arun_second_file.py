while True:
    def check_even_or_odd(num) -> str:
        return "even" if num%2 == 0 else "odd"

    n = int(input('ENer the number to check even or not : '))
    res = check_even_or_odd(n)
    print(res)
    
    print('The Given Number is ',res)
    print('The above syntax is made by second branch')