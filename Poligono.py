 # Crea una única función (importante que sólo sea una) que sea capaz
 # de calcular y retornar el área de un polígono.
 # - La función recibirá por parámetro sólo UN polígono a la vez.
 # - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # - Imprime el cálculo del área de un polígono de cada tipo.

def polygono (poly):
    if poly=="triangulo":
        print ("** Triángulo **")
        base =float(input ("Base: "))
        altura = float(input ("Altura: "))
        return ((base*altura)/2)
    elif poly=="cuadrado":
        print ("** Cuadrado **")
        base =float(input ("Lado: "))
        return base*base
    elif poly=="rectangulo":
        print ("** Rectangulo **")
        base =float(input ("Base: "))
        altura = float(input ("Altura: "))
        return base*altura
    else:
        print ("La información propocionada no es valida")


polygon = input ("Dame el polígono a obtner el area (triangulo, cuadrado o rectangulo)")
resultado = polygono (polygon)
print  ("El área el polígono proporcionado es: {}" .format(resultado))


