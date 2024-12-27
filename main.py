# main ile of the project
# all rights fre reversed
#===================================

# import all nessesary libs and praktik
import praktik as m1
import practik2 as m2
import practik3  as m3       


def main():
    user_choise = input("выберите модуль от 1-3:= ")
    if user_choise.lower() == '1':
        user_temp = float(input("вы выбрали модуль который определяет четное ли число"))
        m1.main()
    elif user_choise.lower() == '2':
        user_temp = float(input("вы выбрали модуль который определяет простое или составное число"))
        m2.main()
    else:
        user_choise.lower() == '3'
        user_temp = float(input("вы выбрали модуль который определяет сумму всех чисел числа"))
        m3.main()
 

if __name__== "__main__":
    main()