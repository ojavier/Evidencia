from random import shuffle
import turtle

from freegames import path

"""
Memoria

Código editado por Luis Adrián Uribe Cruz para la semana Tec
Herramientas computacionales: el arte de la programación (Gpo 201)
"""

taps = 0
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """
    Dibuja un recuadro blaco con un contorno negro.

    El cuadro se dibuja en las coordenadas específicadas.

    Parámetros:
    x (int): La coordenada x de la esquina inferior izquierda.
    y (int): La coordenada y de la esquina inferior izquierda.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


def index(x, y):
    """
    Convierte las coordenadas en índices.

    Con las coordenadas dadas se obtiene el índice para la casilla.

    Parámetros:
    x (int): La coordenada x de la esquina inferior izquierda.
    y (int): La coordenada y de la esquina inferior izquierda.
    """
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """
    Convierte el conteo de las casillas en coordenadas (x,y).

    Operación inversa de la función index()

    Parámetros:
    count(int): El índice de la posición de la casilla.
    """
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """
    Actualiza el estado de la casilla al seleccionarla.

    Invierte su estado como marcada o escondida.

    x (int): La coordenada x de la esquina inferior izquierda.
    y (int): La coordenada y de la esquina inferior izquierda.
    """
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """
    Crea la imagen a revelar y las casillas.

    Coloca la imagen de fondo y la cubre con 64 casillas.
    Verifica el estado de las casillas para saber dibujarlas.

    No posee parámetros.
    """
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.up()
    turtle.goto(-200, -240)
    turtle.write("Toques: ", font=('Arial', 20, 'normal'), move=True)
    turtle.write(taps, font=('Arial', 20, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 100)


shuffle(tiles)
turtle.setup(420, 520, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()
