# Crie um código para classificar 5 números. O usuário pode escolher em
# classificar os valores na ordem crescente ou decrescente.

# obs:Utilize apenas a estrutura condicional IF.


num1 = float(input('Insira o 1° número:'))
num2 = float(input('Insira o 2° número:'))
num3 = float(input('Insira o 3° número:'))
num4 = float(input('Insira o 4° número:'))
num5 = float(input('Insira o 5° número:'))
ordenarRegistros = input('Crescente (C) ou Decrescente (D): ').upper()
print(ordenarRegistros)
# primeiro sendo o maior
if ordenarRegistros == 'D':
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        if num2 > num3 and num2 > num4 and num2 > num5:
            if num3 > num4 and num3 > num5:
                if num4 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 > num4 :
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num5}, 5° valor {num4}.')
            if num4 > num3 and num4 > num5:
                if num3 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 > num3 :
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num5}, 5° valor {num3}.')
            if num5 > num3 and num5 > num4:
                if num4 > num3:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num4}, 5° valor {num3}.')
                elif num3 > num4:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num3}, 5° valor {num4}.')
        if num3 > num2 and num3 > num4 and num3 > num5 :
            if num2 > num4 and num2 > num5 :
                if num4 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 > num4:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num5}, 5° valor {num4}.')
            if num4 > num2 and num4 > num5:
                if num2 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num2}, 5° valor {num5}.')
                elif num5 > num2:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num5}, 5° valor {num2}.')
            if num5 > num2 and num5 > num4:
                if num2 > num4:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num2}, 5° valor {num4}.')
                elif num4 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num4}, 5° valor {num2}.')
        if num4 > num5 and num4 > num3 and num4 > num2 :
            if num5 > num3 and num5 > num2:
                if num3 > num2:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 > num3:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num2}, 5° valor {num3}.')
            if num3 > num5 and num3 >  num2:
                if num5 > num2:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num5}, 5° valor {num2}.')
                elif num2 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num2}, 5° valor {num5}.')
            if num2 > num5 and num2 > num3:
                if num5 > num3:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num5}, 5° valor {num3}.')
                elif num3 > num5:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num3}, 5° valor {num5}.')
        if num5 > num4 and num5 > num3 and num5 > num2 :
            if num4 > num3 and num4 > num2 :
                if num3 > num2:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 > num3:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num2}, 5° valor {num3}.')
            if num3 > num4 and num3 > num2:
                if num4 > num2:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num4}, 5° valor {num2}.')
                elif num2 > num4 :
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num2}, 5° valor {num4}.')
            if num2 > num3 and num2 > num4 :
                if num3 > num4:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num3}, 5° valor {num4}.')
                elif num4 > num3:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num4}, 5° valor {num3}.')

    # segundo sendo o maior

    if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        if num1 > num3 and num1 > num4 and num1 > num5:
            if num3 > num4 and num3 > num5:
                if num4 > num5:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 > num4 :
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num5}, 5° valor {num4}.')
            if num4 > num3 and num4 > num5:
                if num3 > num5:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 > num3 :
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num5}, 5° valor {num3}.')
            if num5 > num3 and num5 > num4:
                if num4 > num3:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num4}, 5° valor {num3}.')
                elif num3 > num4:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num3}, 5° valor {num4}.')
        if num3 > num1 and num3 > num4 and num3 > num5 :
            if num1 > num4 and num1 > num5 :
                if num4 > num5:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 > num4:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num5}, 5° valor {num4}.')
            if num4 > num1 and num4 > num5:
                if num1 > num5:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num1}, 5° valor {num5}.')
                elif num5 > num1:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num5}, 5° valor {num1}.')
            if num5 > num1 and num5 > num4:
                if num1 > num4:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num1}, 5° valor {num4}.')
                elif num4 > num1:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num4}, 5° valor {num1}.')
        if num4 > num5 and num4 > num3 and num4 > num1 :
            if num5 > num3 and num5 > num1:
                if num3 > num1:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 > num3:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num1}, 5° valor {num3}.')
            if num3 > num5 and num3 >  num1:
                if num5 > num1:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num5}, 5° valor {num1}.')
                elif num1 > num5:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num1}, 5° valor {num5}.')
            if num1 > num5 and num1 > num3:
                if num5 > num3:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num5}, 5° valor {num3}.')
                elif num3 > num5:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num3}, 5° valor {num5}.')
        if num5 > num4 and num5 > num3 and num5 > num1 :
            if num4 > num3 and num4 > num1 :
                if num3 > num1:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 > num3:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num1}, 5° valor {num3}.')
            if num3 > num4 and num3 > num1:
                if num4 > num1:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num4}, 5° valor {num1}.')
                elif num1 > num4 :
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num1}, 5° valor {num4}.')
            if num1 > num3 and num1 > num4 :
                if num3 > num4:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num3}, 5° valor {num4}.')
                elif num4 > num3:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num4}, 5° valor {num3}.')

    # terceiro sendo o maior

    if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        if num1 > num2 and num1 > num4 and num1 > num5:
            if num2 > num4 and num2 > num5:
                if num4 > num5:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 > num4 :
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num5}, 5° valor {num4}.')
            if num4 > num2 and num4 > num5:
                if num2 > num5:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num2}, 5° valor {num5}.')
                elif num5 > num2 :
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num5}, 5° valor {num2}.')
            if num5 > num2 and num5 > num4:
                if num4 > num2:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num4}, 5° valor {num2}.')
                elif num2 > num4:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num2}, 5° valor {num4}.')
        if num2 > num1 and num2 > num4 and num2 > num5 :
            if num1 > num4 and num1 > num5 :
                if num4 > num5:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 > num4:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num5}, 5° valor {num4}.')
            if num4 > num1 and num4 > num5:
                if num1 > num5:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num1}, 5° valor {num5}.')
                elif num5 > num1:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num5}, 5° valor {num1}.')
            if num5 > num1 and num5 > num4:
                if num1 > num4:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num1}, 5° valor {num4}.')
                elif num4 > num1:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num4}, 5° valor {num1}.')
        if num4 > num5 and num4 > num2 and num4 > num1 :
            if num5 > num2 and num5 > num1:
                if num2 > num1:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 > num2:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num1}, 5° valor {num2}.')
            if num2 > num5 and num2 >  num1:
                if num5 > num1:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num5}, 5° valor {num1}.')
                elif num1 > num5:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num1}, 5° valor {num5}.')
            if num1 > num5 and num1 > num2:
                if num5 > num2:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num5}, 5° valor {num2}.')
                elif num2 > num5:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num2}, 5° valor {num5}.')
        if num5 > num4 and num5 > num2 and num5 > num1 :
            if num4 > num2 and num4 > num1 :
                if num2 > num1:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 > num2:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num1}, 5° valor {num2}.')
            if num2 > num4 and num2 > num1:
                if num4 > num1:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num4}, 5° valor {num1}.')
                elif num1 > num4 :
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num1}, 5° valor {num4}.')
            if num1 > num2 and num1 > num4 :
                if num2 > num4:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num2}, 5° valor {num4}.')
                elif num4 > num2:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num4}, 5° valor {num2}.')

# quarto sendo maior

    if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        if num1 > num2 and num1 > num3 and num1 > num5:
            if num2 > num3 and num2 > num5:
                if num3 > num5:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 > num3 :
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num5}, 5° valor {num3}.')
            if num3 > num2 and num3 > num5:
                if num2 > num5:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num2}, 5° valor {num5}.')
                elif num5 > num2 :
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num5}, 5° valor {num2}.')
            if num5 > num2 and num5 > num3:
                if num3 > num2:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 > num3:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num2}, 5° valor {num3}.')
        if num2 > num1 and num2 > num3 and num2 > num5 :
            if num1 > num3 and num1 > num5 :
                if num3 > num5:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 > num3:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num5}, 5° valor {num3}.')
            if num4 > num1 and num3 > num5:
                if num1 > num5:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num1}, 5° valor {num5}.')
                elif num5 > num1:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num5}, 5° valor {num1}.')
            if num5 > num1 and num5 > num3:
                if num1 > num3:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num1}, 5° valor {num3}.')
                elif num3 > num1:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num3}, 5° valor {num1}.')
        if num3 > num5 and num3 > num2 and num3 > num1 :
            if num5 > num2 and num5 > num1:
                if num2 > num1:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 > num2:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num1}, 5° valor {num2}.')
            if num2 > num5 and num2 >  num1:
                if num5 > num1:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num5}, 5° valor {num1}.')
                elif num1 > num5:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num1}, 5° valor {num5}.')
            if num1 > num5 and num1 > num2:
                if num5 > num2:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num5}, 5° valor {num2}.')
                elif num2 > num5:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num2}, 5° valor {num5}.')
        if num5 > num3 and num5 > num2 and num5 > num1 :
            if num3 > num2 and num3 > num1 :
                if num2 > num1:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 > num2:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num1}, 5° valor {num2}.')
            if num2 > num3 and num2 > num1:
                if num3 > num1:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 > num3 :
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num1}, 5° valor {num3}.')
            if num1 > num2 and num1 > num3 :
                if num2 > num3:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num2}, 5° valor {num3}.')
                elif num3 > num2:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num3}, 5° valor {num2}.')

    #  quinto  sendo o maior

    if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
        if num1 > num2 and num1 > num3 and num1 > num4:
            if num2 > num3 and num2 > num4:
                if num4 > num3:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num4}, 5° valor {num3}.')
                elif num3 > num4 :
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num3}, 5° valor {num4}.')
            if num3 > num2 and num3 > num4:
                if num2 > num4:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num2}, 5° valor {num4}.')
                elif num4 > num2 :
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num4}, 5° valor {num2}.')
            if num4 > num2 and num4 > num3:
                if num3 > num2:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 > num3:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num2}, 5° valor {num3}.')
        if num2 > num1 and num2 > num3 and num2 > num4 :
            if num1 > num3 and num1 > num4 :
                if num3 > num4:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num3}, 5° valor {num4}.')
                elif num4 > num3:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num4}, 5° valor {num3}.')
            if num4 > num1 and num3 > num4:
                if num1 > num4:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num1}, 5° valor {num4}.')
                elif num4 > num1:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num4}, 5° valor {num1}.')
            if num5 > num1 and num4 > num3:
                if num1 > num3:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num1}, 5° valor {num3}.')
                elif num3 > num1:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num3}, 5° valor {num1}.')
        if num3 > num4 and num3 > num2 and num3 > num1 :
            if num4 > num2 and num4 > num1:
                if num2 > num1:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 > num2:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num1}, 5° valor {num2}.')
            if num2 > num4 and num2 >  num1:
                if num4 > num1:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num4}, 5° valor {num1}.')
                elif num1 > num4:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num1}, 5° valor {num4}.')
            if num1 > num4 and num1 > num2:
                if num4 > num2:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num4}, 5° valor {num2}.')
                elif num2 > num4:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num2}, 5° valor {num4}.')
        if num5 > num3 and num4 > num2 and num4 > num1 :
            if num3 > num2 and num3 > num1 :
                if num2 > num1:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 > num2:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num1}, 5° valor {num2}.')
            if num2 > num3 and num2 > num1:
                if num3 > num1:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 > num3 :
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num1}, 5° valor {num3}.')
            if num1 > num2 and num1 > num3 :
                if num2 > num3:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num2}, 5° valor {num3}.')
                elif num3 > num2:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num3}, 5° valor {num2}.')

      # Ordem Crescente

# primeiro sendo o menor
if ordenarRegistros == 'C':
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        if num2 < num3 and num2 < num4 and num2 < num5:
            if num3 < num4 and num3 < num5:
                if num4 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 < num4:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num5}, 5° valor {num4}.')
            if num4 < num3 and num4 < num5:
                if num3 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 < num3:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num5}, 5° valor {num3}.')
            if num5 < num3 and num5 < num4:
                if num4 < num3:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num4}, 5° valor {num3}.')
                elif num3 < num4:
                    print(f'1° valor:{num1}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num3}, 5° valor {num4}.')
        if num3 < num2 and num3 < num4 and num3 < num5:
            if num2 < num4 and num2 < num5:
                if num4 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 < num4:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num5}, 5° valor {num4}.')
            if num4 < num2 and num4 < num5:
                if num2 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num2}, 5° valor {num5}.')
                elif num5 < num2:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num5}, 5° valor {num2}.')
            if num5 < num2 and num5 < num4:
                if num2 < num4:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num2}, 5° valor {num4}.')
                elif num4 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num4}, 5° valor {num2}.')
        if num4 < num5 and num4 < num3 and num4 < num2:
            if num5 < num3 and num5 < num2:
                if num3 < num2:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 < num3:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num2}, 5° valor {num3}.')
            if num3 < num5 and num3 < num2:
                if num5 < num2:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num5}, 5° valor {num2}.')
                elif num2 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num2}, 5° valor {num5}.')
            if num2 < num5 and num2 < num3:
                if num5 < num3:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num5}, 5° valor {num3}.')
                elif num3 < num5:
                    print(f'1° valor:{num1}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num3}, 5° valor {num5}.')
        if num5 < num4 and num5 < num3 and num5 < num2:
            if num4 < num3 and num4 < num2:
                if num3 < num2:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 < num3:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num2}, 5° valor {num3}.')
            if num3 < num4 and num3 < num2:
                if num4 < num2:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num4}, 5° valor {num2}.')
                elif num2 < num4:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num2}, 5° valor {num4}.')
            if num2 < num3 and num2 < num4:
                if num3 < num4:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num3}, 5° valor {num4}.')
                elif num4 < num3:
                    print(f'1° valor:{num1}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num4}, 5° valor {num3}.')

        # segundo sendo o menor

    if num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        if num1 < num3 and num1 < num4 and num1 < num5:
            if num3 < num4 and num3 < num5:
                if num4 < num5:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 < num4:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num5}, 5° valor {num4}.')
            if num4 < num3 and num4 < num5:
                if num3 < num5:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 < num3:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num5}, 5° valor {num3}.')
            if num5 < num3 and num5 < num4:
                if num4 < num3:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num4}, 5° valor {num3}.')
                elif num3 < num4:
                    print(f'1° valor:{num2}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num3}, 5° valor {num4}.')
        if num3 < num1 and num3 < num4 and num3 < num5:
            if num1 < num4 and num1 < num5:
                if num4 < num5:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 < num4:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num5}, 5° valor {num4}.')
            if num4 < num1 and num4 < num5:
                if num1 < num5:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num1}, 5° valor {num5}.')
                elif num5 < num1:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num5}, 5° valor {num1}.')
            if num5 < num1 and num5 < num4:
                if num1 < num4:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num1}, 5° valor {num4}.')
                elif num4 < num1:
                    print(f'1° valor:{num2}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num4}, 5° valor {num1}.')
        if num4 < num5 and num4 < num3 and num4 < num1:
            if num5 < num3 and num5 < num1:
                if num3 < num1:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 < num3:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num1}, 5° valor {num3}.')
            if num3 < num5 and num3 < num1:
                if num5 < num1:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num5}, 5° valor {num1}.')
                elif num1 < num5:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num1}, 5° valor {num5}.')
            if num1 < num5 and num1 < num3:
                if num5 < num3:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num5}, 5° valor {num3}.')
                elif num3 < num5:
                    print(f'1° valor:{num2}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num3}, 5° valor {num5}.')
        if num5 < num4 and num5 < num3 and num5 < num1:
            if num4 < num3 and num4 < num1:
                if num3 < num1:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 < num3:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num1}, 5° valor {num3}.')
            if num3 < num4 and num3 < num1:
                if num4 < num1:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num4}, 5° valor {num1}.')
                elif num1 < num4:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num1}, 5° valor {num4}.')
            if num1 < num3 and num1 < num4:
                if num3 < num4:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num3}, 5° valor {num4}.')
                elif num4 < num3:
                    print(f'1° valor:{num2}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num4}, 5° valor {num3}.')

        # terceiro sendo o menor

    if num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        if num1 < num2 and num1 < num4 and num1 < num5:
            if num2 < num4 and num2 < num5:
                if num4 < num5:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 < num4:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num5}, 5° valor {num4}.')
            if num4 < num2 and num4 < num5:
                if num2 < num5:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num2}, 5° valor {num5}.')
                elif num5 < num2:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num5}, 5° valor {num2}.')
            if num5 < num2 and num5 < num4:
                if num4 < num2:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num4}, 5° valor {num2}.')
                elif num2 < num4:
                    print(f'1° valor:{num3}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num2}, 5° valor {num4}.')
        if num2 < num1 and num2 < num4 and num2 < num5:
            if num1 < num4 and num1 < num5:
                if num4 < num5:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num4}, 5° valor {num5}.')
                elif num5 < num4:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num5}, 5° valor {num4}.')
            if num4 < num1 and num4 < num5:
                if num1 < num5:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num1}, 5° valor {num5}.')
                elif num5 < num1:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num5}, 5° valor {num1}.')
            if num5 < num1 and num5 < num4:
                if num1 < num4:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num1}, 5° valor {num4}.')
                elif num4 < num1:
                    print(f'1° valor:{num3}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num4}, 5° valor {num1}.')
        if num4 < num5 and num4 < num2 and num4 < num1:
            if num5 < num2 and num5 < num1:
                if num2 < num1:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 < num2:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num5}, 4° valor {num1}, 5° valor {num2}.')
            if num2 < num5 and num2 < num1:
                if num5 < num1:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num5}, 5° valor {num1}.')
                elif num1 < num5:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num1}, 5° valor {num5}.')
            if num1 < num5 and num1 < num2:
                if num5 < num2:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num5}, 5° valor {num2}.')
                elif num2 < num5:
                    print(f'1° valor:{num3}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num2}, 5° valor {num5}.')
        if num5 < num4 and num5 < num2 and num5 < num1:
            if num4 < num2 and num4 < num1:
                if num2 < num1:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 < num2:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num4}, 4° valor {num1}, 5° valor {num2}.')
            if num2 < num4 and num2 < num1:
                if num4 < num1:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num4}, 5° valor {num1}.')
                elif num1 < num4:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num1}, 5° valor {num4}.')
            if num1 < num2 and num1 < num4:
                if num2 < num4:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num2}, 5° valor {num4}.')
                elif num4 < num2:
                    print(f'1° valor:{num3}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num4}, 5° valor {num2}.')

    # quarto sendo menor

    if num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        if num1 < num2 and num1 < num3 and num1 < num5:
            if num2 < num3 and num2 < num5:
                if num3 < num5:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 < num3:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num5}, 5° valor {num3}.')
            if num3 < num2 and num3 < num5:
                if num2 < num5:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num2}, 5° valor {num5}.')
                elif num5 < num2:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num5}, 5° valor {num2}.')
            if num5 < num2 and num5 < num3:
                if num3 < num2:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 < num3:
                    print(f'1° valor:{num4}, 2° valor:{num1}, 3° valor {num5}, 4° valor {num2}, 5° valor {num3}.')
        if num2 < num1 and num2 < num3 and num2 < num5:
            if num1 < num3 and num1 < num5:
                if num3 < num5:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num3}, 5° valor {num5}.')
                elif num5 < num3:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num5}, 5° valor {num3}.')
            if num4 < num1 and num3 < num5:
                if num1 < num5:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num1}, 5° valor {num5}.')
                elif num5 < num1:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num5}, 5° valor {num1}.')
            if num5 < num1 and num5 < num3:
                if num1 < num3:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num1}, 5° valor {num3}.')
                elif num3 < num1:
                    print(f'1° valor:{num4}, 2° valor:{num2}, 3° valor {num5}, 4° valor {num3}, 5° valor {num1}.')
        if num3 < num5 and num3 < num2 and num3 < num1:
            if num5 < num2 and num5 < num1:
                if num2 < num1:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 < num2:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num5}, 4° valor {num1}, 5° valor {num2}.')
            if num2 < num5 and num2 < num1:
                if num5 < num1:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num5}, 5° valor {num1}.')
                elif num1 < num5:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num1}, 5° valor {num5}.')
            if num1 < num5 and num1 < num2:
                if num5 < num2:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num5}, 5° valor {num2}.')
                elif num2 < num5:
                    print(f'1° valor:{num4}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num2}, 5° valor {num5}.')
        if num5 < num3 and num5 < num2 and num5 < num1:
            if num3 < num2 and num3 < num1:
                if num2 < num1:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 < num2:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num3}, 4° valor {num1}, 5° valor {num2}.')
            if num2 < num3 and num2 < num1:
                if num3 < num1:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 < num3:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num2}, 4° valor {num1}, 5° valor {num3}.')
            if num1 < num2 and num1 < num3:
                if num2 < num3:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num2}, 5° valor {num3}.')
                elif num3 < num2:
                    print(f'1° valor:{num4}, 2° valor:{num5}, 3° valor {num1}, 4° valor {num3}, 5° valor {num2}.')

        #  quinto  sendo o menor

    if num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
        if num1 < num2 and num1 < num3 and num1 < num4:
            if num2 < num3 and num2 < num4:
                if num4 < num3:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num4}, 5° valor {num3}.')
                elif num3 < num4:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num2}, 4° valor {num3}, 5° valor {num4}.')
            if num3 < num2 and num3 < num4:
                if num2 < num4:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num2}, 5° valor {num4}.')
                elif num4 < num2:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num3}, 4° valor {num4}, 5° valor {num2}.')
            if num4 < num2 and num4 < num3:
                if num3 < num2:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num3}, 5° valor {num2}.')
                elif num2 < num3:
                    print(f'1° valor:{num5}, 2° valor:{num1}, 3° valor {num4}, 4° valor {num2}, 5° valor {num3}.')
        if num2 < num1 and num2 < num3 and num2 < num4:
            if num1 < num3 and num1 < num4:
                if num3 < num4:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num3}, 5° valor {num4}.')
                elif num4 < num3:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num1}, 4° valor {num4}, 5° valor {num3}.')
            if num4 < num1 and num3 < num4:
                if num1 < num4:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num1}, 5° valor {num4}.')
                elif num4 < num1:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num3}, 4° valor {num4}, 5° valor {num1}.')
            if num5 < num1 and num4 < num3:
                if num1 < num3:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num1}, 5° valor {num3}.')
                elif num3 < num1:
                    print(f'1° valor:{num5}, 2° valor:{num2}, 3° valor {num4}, 4° valor {num3}, 5° valor {num1}.')
        if num3 < num4 and num3 < num2 and num3 < num1:
            if num4 < num2 and num4 < num1:
                if num2 < num1:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 < num2:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num4}, 4° valor {num1}, 5° valor {num2}.')
            if num2 < num4 and num2 < num1:
                if num4 < num1:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num4}, 5° valor {num1}.')
                elif num1 < num4:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num2}, 4° valor {num1}, 5° valor {num4}.')
            if num1 < num4 and num1 < num2:
                if num4 < num2:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num4}, 5° valor {num2}.')
                elif num2 < num4:
                    print(f'1° valor:{num5}, 2° valor:{num3}, 3° valor {num1}, 4° valor {num2}, 5° valor {num4}.')
        if num5 < num3 and num4 < num2 and num4 < num1:
            if num3 < num2 and num3 < num1:
                if num2 < num1:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num2}, 5° valor {num1}.')
                elif num1 < num2:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num3}, 4° valor {num1}, 5° valor {num2}.')
            if num2 < num3 and num2 < num1:
                if num3 < num1:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num3}, 5° valor {num1}.')
                elif num1 < num3:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num2}, 4° valor {num1}, 5° valor {num3}.')
            if num1 < num2 and num1 < num3:
                if num2 < num3:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num2}, 5° valor {num3}.')
                elif num3 < num2:
                    print(f'1° valor:{num5}, 2° valor:{num4}, 3° valor {num1}, 4° valor {num3}, 5° valor {num2}.')
else :
    print('Escolha Inválida!!!')
