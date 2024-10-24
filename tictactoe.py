from turtle import up, goto, down, circle, update, setup, color
from turtle import hideturtle, tracer, onscreenclick, done, width
from freegames import line
import tkinter as tk
from tkinter import messagebox

"""
Tic Tac Toe

Código modificado por Alejandro Araiza Escamilla para la semana Tec
Herramientas computacionales: el arte de la programación (Gpo 201)
"""


def grid():
    """
    Dibuja la cuadrícula del juego Tic-Tac-Toe.

    La cuadrícula se compone de dos líneas verticales y dos horizontales.
    """
    line(-67, 200, -67, -200)  # Primera línea vertical
    line(67, 200, 67, -200)    # Segunda línea vertical
    line(-200, -67, 200, -67)  # Primera línea horizontal
    line(-200, 67, 200, 67)    # Segunda línea horizontal


def drawx(x, y):
    """
    Dibuja la letra X en la posición especificada.

    La X se dibuja en color rojo y con un grosor de 5 píxeles.

    Parámetros:
    x (int): La coordenada x de la esquina inferior izquierda.
    y (int): La coordenada y de la esquina inferior izquierda.
    """
    color('red')  # Cambia el color a rojo
    width(5)      # Ajusta el grosor de la línea
    up()          # Levanta el lápiz
    goto(x + 25, y + 25)  # Se mueve a la posición de inicio de la X
    down()        # Baja el lápiz para empezar a dibujar
    line(x + 25, y + 25, x + 108, y + 108)  # Dibuja la primera línea de la X
    line(x + 25, y + 108, x + 108, y + 25)  # Dibuja la segunda línea de la X
    up()          # Levanta el lápiz al terminar


def drawo(x, y):
    """
    Dibuja la letra O en la posición especificada.

    La O se dibuja en color rojo y con un grosor de 5 píxeles.

    Parámetros:
    x (int): La coordenada x de la esquina inferior izquierda.
    y (int): La coordenada y de la esquina inferior izquierda.
    """
    color('red')  # Cambia el color a rojo
    width(5)      # Ajusta el grosor de la línea
    up()          # Levanta el lápiz
    goto(x + 65, y + 25)  # Se mueve a la posición para centrar la O
    down()        # Baja el lápiz para empezar a dibujar
    circle(40)    # Dibuja un círculo con radio 40


def floor(value):
    """
    Redondea un valor a la cuadrícula más cercana
    con tamaño de celda de 133.

    Esto asegura que los símbolos se alineen correctamente
    en las casillas de la cuadrícula.

    Parámetros:
    value (int): El valor a redondear.

    Devuelve:
    int: El valor redondeado a la cuadrícula más cercana.
    """
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}  # Estado que almacena al jugador actual (0 o 1)
players = [drawx, drawo]  # Lista de funciones para dibujar X y O
occupied = {}  # Diccionario para rastrear las casillas ocupadas


def show_error():
    """
    Muestra una ventana emergente de advertencia cuando
    una casilla ya está ocupada.

    La ventana muestra el mensaje "Casilla ocupada, elige otra."
    """
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    messagebox.showwarning("Error", "Casilla ocupada, elige otra.")
    root.destroy()  # Cierra la ventana oculta


def tap(x, y):
    """
    Maneja el evento de clic del usuario en el tablero.

    Si la casilla ya está ocupada, se muestra una advertencia.
    Si está libre, dibuja el símbolo del jugador
    correspondiente y alterna entre X y O.

    Parámetros:
    x (int): La coordenada x donde se hizo clic.
    y (int): La coordenada y donde se hizo clic.
    """
    x = floor(x)  # Redondea la coordenada x a la cuadrícula más cercana
    y = floor(y)  # Redondea la coordenada y a la cuadrícula más cercana

    if (x, y) in occupied:  # Verifica si la casilla ya está ocupada
        show_error()  # Muestra la ventana de error si está ocupada
        return

    player = state['player']  # Obtiene el jugador actual (0 para X, 1 para O)
    draw = players[player]  # Selecciona la función de dibujo correcta (X o O)
    draw(x, y)  # Dibuja el símbolo en la casilla seleccionada
    update()  # Actualiza la pantalla
    occupied[(x, y)] = player  # Marca la casilla como ocupada
    state['player'] = not player  # Alterna el jugador para el próximo turno


setup(420, 420, 370, 0)  # Configura la ventana de Turtle
hideturtle()  # Oculta el cursor de Turtle
tracer(False)  # Desactiva el trazado en tiempo real
grid()  # Dibuja la cuadrícula del tablero
update()  # Actualiza la pantalla
onscreenclick(tap)  # Asigna la función tap al evento de clic
done()  # Finaliza la ejecución de Turtle
