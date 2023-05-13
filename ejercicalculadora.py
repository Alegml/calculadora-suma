num1 = input("1er numero: ")

if num1.isnumeric() or (num1 [0] == '-' and num1[1: ].isnumeric()):
    num1 = float(num1)
else:
    try: 
        num1 = float(num1)
    except ValueError :
        print("No valido")
        exit()

num2 = input("2do numero: ")

if num2.isnumeric() or (num2 [0] == '-' and num2[1: ].isnumeric()):
    num2 = float(num2)
else:
    try: 
        num2 = float(num2)
    except ValueError :
        print("No valido")
        exit()

resultado = num1 + num2 
print("resultado: " , resultado)

