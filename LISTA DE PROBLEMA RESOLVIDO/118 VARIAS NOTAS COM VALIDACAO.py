while True:
    nota1 = float(input(''))
    while nota1 < 0 or nota1 > 10:
        print('nota invalida')
        nota1 = float(input(''))

    nota2 = float(input(''))
    while nota2 < 0 or nota2 > 10:
        print('nota invalida')
        nota2 = float(input(''))

    media = (nota1 + nota2) / 2

    print('media = {:.2f}'.format(media))
    print('novo calculo (1-sim 2-nao)')
    x = int(input())
    while x < 1 or x > 2:
        print('novo calculo (1-sim 2-nao)')
        x = int(input())

    if x == 2:
        break
