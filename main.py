#Listo ya resolví el problema, ahora si funciona el programa
print("Hola Mundo! Version 1.1")
print("Esto ya está funcionado")


# HU-1
# Función para verificar si una cadena es un palíndromo

def palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(palindromo("Ana"))  # True
print(palindromo("Hola"))  # False

print("que día tan loco, ya terminé")
