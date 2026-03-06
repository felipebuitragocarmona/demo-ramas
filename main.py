print("Hello, World! Version 1.0")
print("Esto ya está funcionado")

# HU-1
# Función para verificar si una cadena es un palíndromo

def palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(palindromo("Ana"))  # True
print(palindromo("Hola"))  # False