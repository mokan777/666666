#написать программу которая определяет простое
# или составное число, автор Алексей






# the main function of project
def is_prime(n):
    d = 2 # присваиваем значение d
    while n % d != 0: # если d делит число без остатка то число не простое
        d += 1 # доходим до самого n
       
    return d == n # если мы дошли до числа n то число простое


def main():
    n = int(input('введите число которое хотите узнать: ')) # вводим число
    
    result = is_prime(n)
    print('false - число составное, true - число простое:',result)#  ввывод чисел

    



if __name__== "__main__":
    main()