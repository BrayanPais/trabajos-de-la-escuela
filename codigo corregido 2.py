def iniciar():
 entrada1 = input("Ingresa un valor de referencia textual: ")
 entrada2 = input("Ingresa otra unidad: ")
 x = preparar_datos(entrada1) # ¿Por qué usar esto aquí?
 y = preparar_datos(entrada2)
 resultado = mezcla_datos(x, y)
 print("Resultado no final: ", resultado)
 # El siguiente bloque debe imprimir solo si 'entrada1' está en 'entrada2'
 if entrada1 in entrada2:
  print("Coincidencia detectada.") # Error intencional de indentación
def preparar_datos(info):
 # Supone que 'info' será un conjunto, pero realmente espera una lista
 acumulador = ""
 for letra in info:
  acumulador += letra + "-"
 return acumulador[:-1]
def mezcla_datos(a, b):
 # Compara dos cosas que no se deberían comparar directamente
 if len(a) > len(b):
  return a + b
 elif len(a) == len(b):
  return a * 2
 else:
  return b + a

iniciar()  