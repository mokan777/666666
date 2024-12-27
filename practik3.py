# написать функцию которая определяет суммувсех чисел числа
# автор Алексей





# the main function of project
def multiply(n):
    c = 0 # начинаем с 0
    for i in str(n): # переводим число в строку
        c += int(i) # находим сумму чисел числа
    return c


def main():
    n = int(input('введите число которое хотите узнать: ')) # вводим число
    result = multiply(n)
    print('сумма всех чисел цифр в числе:',result) #  ввывод чисел




if __name__== "__main__":
        main()