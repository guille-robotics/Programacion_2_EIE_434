import argparse  # Librería que permite recibir argumentos desde la línea de comandos

# Creamos el objeto parser.
# Este objeto será el encargado de interpretar los argumentos que el usuario
# entregue cuando ejecute el programa desde la terminal.
parser = argparse.ArgumentParser(description="Calculadora de resistencias")

# -------------------------------------------------------------------
# Argumento 1: tipo de conexión
# -------------------------------------------------------------------

parser.add_argument(
    "--tipo",  # Nombre del argumento que se usará en la terminal
    type=str,  # Indicamos que el argumento debe ser un texto (string)

    # choices limita los valores posibles que puede ingresar el usuario.
    # Si el usuario escribe algo distinto a "serie" o "paralelo",
    # argparse mostrará automáticamente un error.
    choices=["serie", "paralelo"],

    # required=True significa que este argumento es obligatorio.
    # Si el usuario no lo escribe al ejecutar el programa,
    # el programa mostrará un mensaje de error.
    required=True,

    # Texto de ayuda que aparece cuando el usuario ejecuta:
    # python desafio.py --help
    help="Tipo de conexión"
)

# -------------------------------------------------------------------
# Argumento 2: lista de resistencias
# -------------------------------------------------------------------

parser.add_argument(
    "--resistencias",  # Nombre del argumento en la terminal
    type=float,  # Cada valor ingresado será convertido a número decimal

    # nargs="+" indica que el usuario puede ingresar UNO o MÁS valores.
    # Por ejemplo:
    # python desafio.py --tipo serie --resistencias 10 20 30
    #
    # Todos estos valores se guardarán dentro de una lista.
    nargs="+",

    # Este argumento también es obligatorio
    required=True,

    help="Lista de resistencias"
)

# -------------------------------------------------------------------
# Aquí argparse procesa los argumentos ingresados en la terminal
# y los guarda dentro de la variable args
# -------------------------------------------------------------------

args = parser.parse_args()

# Después de esta línea podemos acceder a los argumentos así:
# args.tipo
# args.resistencias

# -------------------------------------------------------------------
# Cálculo de la resistencia equivalente
# -------------------------------------------------------------------

# Si el usuario seleccionó conexión en serie
if args.tipo == "serie":

    # La resistencia equivalente es simplemente la suma de todas
    # las resistencias del circuito
    req = sum(args.resistencias)

# Si el usuario seleccionó conexión en paralelo
elif args.tipo == "paralelo":

    suma = 0

    # Para paralelo debemos sumar los inversos de cada resistencia
    for r in args.resistencias:
        suma += 1 / r

    # Finalmente invertimos la suma
    req = 1 / suma

# -------------------------------------------------------------------
# Mostramos el resultado final
# -------------------------------------------------------------------

print(f"Resistencia equivalente ({args.tipo}): {req:.2f} Ω")