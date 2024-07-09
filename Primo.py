 # Escribe un programa que se encargue de comprobar si un número es o no primo.
 # Hecho esto, imprime los números primos entre 1 y 100.


try :
    while True:
        number = int(input ("Numero a verificar: "))
        if number == 0: 
            print ("El número debe de ser mayor a 0")
        else:
            break
      
    if number == 2:
        print ("El número {} es un número primo " .format(number))
    else:
        for i in range (2, number):
            if (number%i)==0:
                print ("El número {} es divisible entre {} por lo tanto NO es un número primo " .format(number, i))
                break
            else:
                if i == (number-1): print ("El número {} es un número primo " .format(number))
        
except ValueError:
    print ("Favor de insertar un número entero!!")
