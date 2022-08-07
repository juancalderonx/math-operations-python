print('Bienvenido al menú de operaciones matemáticas')
print()


def menu():
    print('Por favor, elija una opción')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Potenciar')
    print('6. SALIR')
    opcion = int(input())

    match opcion:
        case 1:
            num1 = int(input('Digite un número para sumar '))
            num2 = int(input('Digite otro número para sumar '))
            suma(num1, num2)
        case 2:
            num1 = int(input('Digite un número para restar '))
            num2 = int(input('Digite otro número para restar '))
            resta(num1, num2)
        case 3:
            num1 = int(input('Digite un número para multiplicar '))
            num2 = int(input('Digite otro número para multiplicar '))
            multiplicacion(num1, num2)
        case 4:
            num1 = int(input('Digite un número para dividir '))
            num2 = int(input('Digite otro número para dividir '))
            division(num1, num2)
        case 5:
            num1 = int(input('Digite un número a potenciar '))
            num2 = int(input('Digite el número para potenciar '))
            potenciacion(num1, num2)
        case 6:
            print('Saliendo....')
            quit()
        case _:
            print('Por favor, elija una opción correcta')
            menu()


def suma(num1, num2):
    print('------------')
    print(num1 + num2)
    print('------------')
    menu()


def resta(num1, num2):
    print('------------')
    print(num1 - num2)
    print('------------')
    menu()


def multiplicacion(num1, num2):
    print('------------')
    print(num1 * num2)
    print('------------')
    menu()


def division(num1, num2):
    print('------------')
    print(num1 / num2)
    print('------------')
    menu()


def potenciacion(num1, num2):
    print('------------')
    print(num1**num2)
    print('------------')
    menu()


menu()
