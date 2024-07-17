 # Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 # - Un Anagrama consiste en formar una palabra reordenando TODAS
 #   las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.


firststring = input ("Introduce la primer palabra: ")
scndstring = input ("Introduce la segunda palabra: ")

scdlngt = len(scndstring)
firststring = firststring.lower()
scndstring = scndstring.lower()
result = 1
try :
    for letter in firststring:       
        if scndstring.index(letter):
            result += 1    

    print("La palabras forman un anagrama", ) if result == scdlngt else print("Las palabras no forman un anagrama")
except ValueError:
    print ("Las palabras no forman un anagrama")