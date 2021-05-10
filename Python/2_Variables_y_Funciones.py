
# Variables Globales
# Estas pueden encontrarse en cualquier archivo .py y funcionaran para todo el programa.
calculo_a_unidades = 24
unidades = "horas"

# Función
# Bloque de código que se ejecuta cuando es llamado.
def dias_a_unidades(numero_dias):
    print("Respuesta dentro de la función.")

    if(dias > 0):
        print(f"En {numero_dias} día(s) hay {numero_dias * calculo_a_unidades} de {unidades}.\n")
    elif dias == 0: 
        print("No se permite el valor 0 para el número de días.\n")
    else:
        print("No se permiten valores negativos.\n")


def dias_a_unidades_ret(numero_dias):
    print("La función regresa los resultados.")

    if(dias > 0):
        return f"En {numero_dias} día(s) hay {numero_dias * calculo_a_unidades} de {unidades}.\n"
    elif dias == 0:
        return "No se permite el valor 0 para el número de días.\n"
    else:
        return "No se permiten valores negativos.\n"


# Casting
# Convertir un dato en otro tipo de dato, input siempre toma la informaicón que recibe como string.
# El dato que actualmente estamos pidiendo es un entero, por lo que se convierte con int().
dias = int( input("\nNúmero de días: ") )
print("\n")

# Llamado de las funciones
dias_a_unidades(dias)

resultado = dias_a_unidades_ret(dias)
print(resultado)