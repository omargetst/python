 # Escribe un programa que se encargue de comprobar si un número es o no primo.
 # Hecho esto, imprime los números primos entre 1 y 100.
 # Creado con funciones

def primo (valor):
    if valor == 2:
        return -1
    else:
        for i in range (2, valor):       
            if (valor%i)==0:
                return i
                break
            else:
                if i == (valor-1): return -1

try :
    while True:
        number = int(input ("Numero a verificar: "))
        if number == 0: 
            print ("El número debe de ser mayor a 0")
        else:
            break
      
    divi = primo (number)
    print("El {} es un número Primo" .format(number)) if divi == -1 else print ("El número {} es divisible entre {} por lo tanto NO es un número primo " .format(number, divi))

    divid = 0
    print ("Los números primos entre el 1 y el 100:")
    for c in range (1, 100):
        divid = primo (c)
        if divid == -1: 
            print (c, end=" ")
   
except ValueError:
    print ("Favor de insertar un número entero!!")
