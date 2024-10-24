from turtle import up, goto, down, circle, update, setup, color
from turtle import hideturtle, tracer, onscreenclick, done, width
from freegames import line

"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

"""
Codigo modificado por Alejandro Araiza Escamilla para la semana Tec
Herramientas computacionales: el arte de la programacion (Gpo 201)
"""


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('red')
    width(5)
    up()
    goto(x + 25, y + 25)
    down()
    line(x + 25, y + 25, x + 108, y + 108)
    line(x + 25, y + 108, x + 108, y + 25)
    up()


def drawo(x, y):
    """Draw O player."""
    color('red')
    width(5)
    up()
    goto(x + 65, y + 25)
    down()
    circle(40)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
