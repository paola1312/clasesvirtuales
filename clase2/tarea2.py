# Eres la el guarda de la discoteca la 21, vas a preguntar el nombre y la edad a los jovenes
# Si el joven es mayor de edad decirle Bienvenido + nombre del joven + eres mayor de edad
# Si el joven es menor de edad decirle Vaya pa la casa + nombre del joven + usted tiene tanta edad y no puede ingresar



#vas a preguntar el nombre y la edad a los jovenes

nombre = input ("Cual es tu nombre  ")
edad = int(input ("cual es tu edad   "))

# Si el joven es mayor de edad decirle Bienvenido + nombre del joven + eres mayor de edad
# Si el joven es menor de edad decirle Vaya pa la casa + nombre del joven + usted tiene tanta edad y no puede ingresar


if edad >= 18:
    print (" Bienvenido  "+ nombre   + " Usted es mayor   ")
else:
    print (" Vaya para la casa  " + nombre   + " usted tiene "+str (edad) +" y no puede ingresar  ")